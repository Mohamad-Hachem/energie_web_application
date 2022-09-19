# let's import our needed modules
import pymongo

import os
# let's create our database that needed
database = pymongo.MongoClient(host=os.environ.get("MONGO_HOST"),
                               port=27017,
                               username="root",
                               password="pass",
                               authSource="admin")

# creating our database name
db = database['energie_database']

# creating a collection
mycol = db["record"]
