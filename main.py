from fastapi import FastAPI
import requests

app = FastAPI()

URL = "http://api.open-notify.org"

@app.get("/iss")
async def get_crew():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        print(response.text)
        return response.text
    except requests.RequestException:
        return response.status_code
