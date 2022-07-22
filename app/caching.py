from re import I
import redis
import sys
from .config import REDIS_HOST,REDIS_PORT

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=0,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.ConnectionError:
        print("Connection Error!")
        sys.exit(1)

def get_response_from_cache(request):
    """Data from redis."""

    return client.get(request)

client = redis_connect()
timeout = 240