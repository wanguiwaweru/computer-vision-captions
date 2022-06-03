SUBSCRIPTION_KEY = "a6498ac0712546258fd220d13d2e90bb"
ENDPOINT = "https://cv-alt-text-generator.cognitiveservices.azure.com/"
REQUEST_URL = ENDPOINT +"vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest"
headers = {"Ocp-Apim-Subscription-Key":SUBSCRIPTION_KEY}
params = {"visualFeatures":"Categories,Description,Color"}
