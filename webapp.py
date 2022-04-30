from flask import Flask
from models.media import Media
from models.mediamanager import MediaManager
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    pass


if __name__ == "__main__":
    app.run(debug=True)