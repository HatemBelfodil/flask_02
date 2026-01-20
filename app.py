from flask import Flask
from pymongo_get_database import get_database
from flask_pymongo import PyMongo

app = Flask(__name__)
dbname = get_database("publication_manager")

@app.route("/")
def index():
    collection = dbname['mesrs_journals']
    cursor = collection.find({}).limit(10)
    list_of_journaux = []
    for journal in cursor:
        journal['_id'] = str(journal['_id'])
        list_of_journaux.append(journal)

    return "Salem Alaykoum wa rahmatou allah "+str(len(list_of_journaux))

