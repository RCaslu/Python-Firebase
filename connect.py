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

def upload_json_to_firebase(json_file):
    with open(json_file, 'r', encoding='utf-16') as file:
        data = json.load(file)  
        ref.set(data)  
    print("Dados enviados com sucesso!")

def fetch_data_from_firebase():
    data = ref.get()  
    print("Dados recuperados do Firebase:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

upload_json_to_firebase('dados.json')

fetch_data_from_firebase()