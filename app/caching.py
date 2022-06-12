import redis
import sys

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
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
    
    return client.get(request.sha_key)

client = redis_connect()