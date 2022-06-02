from dotenv import dotenv_values

config = dotenv_values(".env")

SUBSCRIPTION_KEY = config['SUBSCRIPTION_KEY']
REQUEST_URL = config['REQUEST_URL']
headers = config['headers']
params = config['params']
