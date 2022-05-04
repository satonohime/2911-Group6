from flask import Flask, render_template
from models.media import Media
from models.mediamanager import MediaManager
from models.mediatype import MediaType
import json

app = Flask(__name__)

PRESET_TYPE_DATA = [
    ['music', 'artist', 'album', 'genre'],
    ['book', 'author', 'publisher', 'genre'],
    ['game', 'main_platform', 'publisher' ,'genre']
]

@app.route("/")
def homepage():
    mediamnger = MediaManager()
    media_entries = mediamnger.media
    return render_template('index.html', data=media_entries, types=PRESET_TYPE_DATA)

@app.route("/<string:media_type>/<string:name>", methods=["GET"])
def get_entry(media_type, name):
    mediamnger = MediaManager()
    entry = mediamnger.view_media(name, media_type)
    print(entry.field_1)
    if entry is None:
        return 'Entry not found', 404
    return render_template('entry.html', name=name, data=entry.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
