from flask import Flask, render_template
from models.media import Media
from models.mediamanager import MediaManager
from models.mediatype import MediaType
import json

app = Flask(__name__)


@app.route("/")
def homepage():
    mediamnger = MediaManager()
    media_entries = mediamnger.list_by_type('book')
    return render_template('index.html', data=media_entries)

@app.route("/book/<string:book_name>", methods=["GET"])
def get_entry(book_name):
    mediamnger = MediaManager()
    book = mediamnger.view_media(book_name, 'book')
    print(book.field_1)
    if book is None:
        return 'Book entry not found', 404
    return render_template('entry.html', b_name=book_name, data=book)

if __name__ == "__main__":
    app.run(debug=True)
