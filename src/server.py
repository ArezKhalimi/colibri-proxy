import argparse
from datetime import datetime

import aiohttp
from aiohttp import web
import redis

from jwt_generator import generate_token
from settings import UPSTREAM_URL, REDIS_HOST


session = aiohttp.ClientSession()
redis_cli = redis.Redis(
    host=REDIS_HOST, port=6379, db=0, decode_responses=True
)


def refresh_status():
    """
    Set initial data for state
    """
    redis_cli.set('start_time', str(datetime.now()))
    redis_cli.set('processed_count', 0)


async def clean_session(app):
    await session.close()


async def proxy(request):
    """
    Simple proxy emdpoint
    """
    json_body = await request.json()
    upstream_headers = {
        head: request.headers[head] for head in ['Accept', 'Accept-Encoding']
    }
    upstream_headers['x-my-jwt'] = await generate_token(json_body)
    resp = await session.post(
        UPSTREAM_URL, json=json_body, headers=upstream_headers
    )
    result = await resp.text()
    redis_cli.incr('processed_count', 1)

    return web.Response(body=result, status=resp.status, headers=resp.headers)


async def status(request):
    """
    Status endpoint for:
        - time from start
        - number of requests processed
    """
    info = {
        'start_time': str(redis_cli.get('start_time')),
        'processed_count': redis_cli.get('processed_count'),
    }
    return web.json_response(info)


app = web.Application()
# close session at the end of clean-up app
app.on_cleanup.append(clean_session)

# simple routing
app.add_routes([
    web.post('/', proxy),
    web.get('/status', status)
])
refresh_status()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Colibri proxy server")
    parser.add_argument('--port')
    args = parser.parse_args()

    web.run_app(app, port=args.port)
