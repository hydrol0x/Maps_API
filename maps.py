import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('MAPS_API_KEY')
SEARCH_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json?"


def getID(userInput, inputType="textquery"):
    response = requests.get(
        SEARCH_URL+"input={userInput}&inputtype={inputType}&key={API_KEY}".format(userInput=userInput, inputType=inputType, API_KEY=API_KEY))
    parsed = json.loads(response.text)
    return parsed["candidates"][0]["place_id"]


def getPlace(placeID, fields="name,formatted_phone_number,formatted_address"):
    response = requests.get(
        DETAILS_URL+"place_id={placeID}&fields={fields}&key={API_KEY}".format(placeID=placeID, fields=fields, API_KEY=API_KEY))
    parsed = json.loads(response.text)
    return parsed["result"]


def search(query, json=False):
    PID = getID(query)
    search = getPlace(PID)
    if json:
        return json.dumps(search)
    else:
        return search


if __name__ == "__main__":
    userPlace = input("Enter Query: ")
    print([val for val in search(userPlace).values()])
