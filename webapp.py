from flask import Flask, redirect, render_template, request
from models.media import Media
from models.mediamanager import MediaManager
from models.mediatype import MediaType
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import certifi

app = Flask(__name__)
app.config["SECRET_KEY"] = "TAMIM"
app.config[
    "MONGO_URI"
] = "mongodb+srv://adminUser:adminpw@agile.c5ssi.mongodb.net/agileDb?retryWrites=true&w=majority"
mongodb_client = PyMongo(app, tlsCAFile=certifi.where())

db = mongodb_client.db.agileCollection

def init_manager():
    data = [doc for doc in db.find()]
    mediamnger = MediaManager(data=data)
    mediamnger.set_local_keys()
    return mediamnger

@app.route("/", methods=["GET"])
def homepage():
    mediamnger = init_manager()
    media_entries = mediamnger.media
    return (
        render_template(
            "index.html", data=media_entries, types=mediamnger.types, manager=mediamnger
        ),
        200,
    )

@app.route("/about", methods=["GET"])
def about():
    return (render_template("about.html"),200)


@app.route("/updated", methods=["POST"])
def homepage_updated():
    mediamnger = init_manager()
    type = request.form["type"]
    name = request.form["name"]
    f1 = request.form["field_1"]
    f2 = request.form["field_2"]
    f3 = request.form["field_3"]
    
    mediamnger.add_media(name, type, f1, f2, f3)
    mediamnger.set_local_keys()
    db.insert_one(mediamnger.media[-1].to_dict())

    return redirect("/", 302)
    


@app.route("/editentry/<int:local_key>", methods=["PUT"])
def edit_entry(local_key):
    mediamnger = init_manager()
    entry_to_edit = mediamnger.view_media(local_key)

    entry_to_edit.name = request.form["name"]
    entry_to_edit.field_1 = request.form["field_1"]
    entry_to_edit.field_2 = request.form["field_2"]
    entry_to_edit.field_3 = request.form["field_3"]

    db.update_one({ "_id": ObjectId(entry_to_edit._id) }, 
            { "$set": { "name": entry_to_edit.name,
             entry_to_edit.type.field_1: entry_to_edit.field_1,
             entry_to_edit.type.field_2: entry_to_edit.field_2,
             entry_to_edit.type.field_3: entry_to_edit.field_3 } })

    return "", 204


@app.route("/addentry", methods=["GET", "POST"])
def form_display():
    mediamnger = init_manager()
    select_media = request.form["medias"]
    media_type = mediamnger.search_for_type(select_media)
    return render_template("create.html", type=media_type), 200


@app.route("/editentry/<int:local_key>", methods=["GET"])
def edit_form_display(local_key):
    mediamnger = init_manager()
    entry = mediamnger.view_media(local_key)
    return render_template("edit.html", data=entry), 200


@app.route("/deleteentry/<int:local_key>", methods=["DELETE"])
def delete_entry(local_key):
    mediamnger = init_manager()
    entry = mediamnger.view_media(local_key)
    db.delete_one({ "_id": ObjectId(entry._id) })
    mediamnger.delete_media(local_key)
    return "", 201


@app.route("/<int:local_key>", methods=["GET"])
def get_entry(local_key):
    mediamnger = init_manager()
    entry = mediamnger.view_media(local_key)
    if entry is None:
        return "Entry not found", 404
    return render_template("entry.html", data=entry.to_dict(), localkey = entry.local_key), 200


if __name__ == "__main__":
    app.run(debug=True)
