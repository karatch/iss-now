from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/iss")
async def get_iss(): # get the current location of the ISS
    api_url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print(response.text)
        return response.text
    except requests.RequestException:
        return response.status_code
