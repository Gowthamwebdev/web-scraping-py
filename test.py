import os
import cv2
import requests
import matplotlib.pyplot as plt
from deepface import DeepFace

def img_to_song(image_location,
                api_url='https://spotify81.p.rapidapi.com/search',
                api_key=None,
                api_host="spotify81.p.rapidapi.com",
                offset=0,
                limit=10,
                numberOfTopResults=5):
    # read image
    img = cv2.imread(image_location)

    # analyze the image using DeepFace
    result = DeepFace.analyze(img, actions=['emotion'])

    # extracting emotion with highest percentage
    query = max(result['emotion'], key=result['emotion'].get)

    url = str(api_url)

    querystring = {"q": f"{query}", "type": "multi",
                   "offset": str(offset), "limit": str(limit),
                   "numberOfTopResults": str(numberOfTopResults)}

    headers = {
        "X-RapidAPI-Key": str(api_key),
        "X-RapidAPI-Host": str(api_host)
    }

    # send a HTTP GET request to the specified URL
    response = requests.get(url, headers=headers, params=querystring)

    # check if the request was successful
    if response.status_code == 200:
        output = []
        for i in range(limit):
            output.append(f"""song name: {response.json()['tracks'][i]['data']['name']}
                            album name:{response.json()['tracks'][i]['data']['albumOfTrack']['name']}\n""")
        return output
    else:
        return f"Error: {response.status_code}"

# get the API key from environment variable
api_key = os.getenv('API_KEY')

loc = 'C:\Users\gowth\OneDrive\Pictures\1675181391382.jpg'
k = img_to_song(loc, api_key=api_key)
print(k)
