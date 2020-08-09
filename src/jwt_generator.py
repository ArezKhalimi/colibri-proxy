import time

from jose.jwt import encode as jwt_encode

from settings import SIGNATURE, JTI, ALGORITHM


async def generate_token(payload):
    """
    Generate JWT with specified claims
    """
    claims = {
        'iat': int(time.time()),
        'jti': JTI,
        'payload': payload
    }
    jwt = jwt_encode(claims, SIGNATURE, algorithm=ALGORITHM)

    return jwt
