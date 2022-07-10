SUBSCRIPTION_KEY = "6473b62078ac4881971689155789c7cc"
ENDPOINT = "https://cv-captions.cognitiveservices.azure.com/"
REQUEST_URL = ENDPOINT +"vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest"
headers = {"Ocp-Apim-Subscription-Key":SUBSCRIPTION_KEY}
params = {"visualFeatures":"Categories,Description,Color"}
