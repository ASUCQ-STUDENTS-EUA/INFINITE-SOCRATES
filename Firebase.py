#50954152
#Signing in for Admin
pip install firebase-admin

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/rassimbelazzoug/Downloads/infinite-socrates-firebase-adminsdk-fbsvc-d737f9b800.json") #Meant to be the path to the firebase Admin Key file. 
firebase_admin.initialize_app(cred)
