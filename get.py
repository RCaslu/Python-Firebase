import firebase_admin
from firebase_admin import db, credentials
import json

cred = credentials.Certificate("cert.json")
firebase_admin.initialize_app(cred, 
                              {"databaseURL": 
                               'https://marketproject-7003e-default-rtdb.firebaseio.com/'
                               }
                               )

ref = db.reference('/')

print(ref.get())
