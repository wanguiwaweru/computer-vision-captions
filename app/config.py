SUBSCRIPTION_KEY = "cddc281b7ef54deabbd351733597a15d"
ENDPOINT = "https://generate-captions.cognitiveservices.azure.com/"
REQUEST_URL = ENDPOINT +"vision/v3.2/describe?maxCandidates=4&language=en&model-version=latest"
headers = {"Ocp-Apim-Subscription-Key":SUBSCRIPTION_KEY}
params = {"visualFeatures":"Categories,Description,Color"}
