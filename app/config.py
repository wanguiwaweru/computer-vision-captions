import os

SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
ENDPOINT = os.getenv("ENDPOINT")
REQUEST_URL = ENDPOINT +"vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest"
AUTH_HEADERS = {"Ocp-Apim-Subscription-Key":SUBSCRIPTION_KEY}
DEFAULT_PARAMS = {"visualFeatures":"Categories,Description,Color"}

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PORT = os.getenv("REDIS_PORT",6379)
