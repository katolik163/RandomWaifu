from flask import render_template
from app import app
from app.waifu import get_waifu

@app.route('/')
def index():
    image = get_waifu()
    json_link = 'https://api.waifu.im/search?is_nsfw=null&included_files=' + str(image["image_id"])
    image_size = image["byte_size"] / 1024 / 1024
    return render_template('index.html', image=image, json_link=json_link, image_size=image_size)