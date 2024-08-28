import json
import requests

def get_waifu():
    url = 'https://api.waifu.im/search'
    params = {
        'is_nsfw': 'null' #getting sfw/nsfw image
    }
    response = json.loads(requests.request("GET", url, params=params).text)
    image_data = response["images"][0]
    return image_data