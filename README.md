# computer-vision-captions
This project generates alt-text for images.

To get started, clone the repo and run:
`pip install -r requirements.txt`

To get the endpoint and subscription key from Azure, login to [Azure portal](https://portal.azure.com/) and create a Computer Vision resource and fill in the details.
After the computer vision resource has been created successfully, navigate to the **Keys and Endpoint** and copy the subscription key and endpoint.

Create a .env file in the same directory and add the following:

SUBSCRIPTION_KEY="YOUR_KEY"
ENDPOINT="YOUR_ENDPOINT"

On your terminal run uvicorn app.main:app
Navigate to http://127.0.0.1:8000/docs to view the interactive docs.
On postman create a POST request to http://127.0.0.1:8000/api and add a request body that contains the url and the request id.

##DOCKER

Run `docker compose up --build` 

Navigate to http://127.0.0.1:8000/docs to view the interactive docs.
On postman create a POST request to http://127.0.0.1:8000/api and add a request body that contains the url and the request id.
