import os

from envparse import env

src_path = os.path.dirname(os.path.realpath(__file__))

env.read_envfile(os.path.join(src_path, '.myenv'))

ALGORITHM = env.str('ALG')
DEBUG = env.bool('DEBUG')
JTI = env.str('JTI')
SIGNATURE = env.str('SIGNATURE')
UPSTREAM_URL = env.str('UPSTREAM_URL')
# redis_host will set `redis`(default for docker) if redis host not provided
REDIS_HOST = env('REDIS_HOST', 'redis')
