# This is just a python application to get data from api with link given
# It can be any application like android, java.... 
# It si placed in this project bcoz of demo purpose (this application can be inside or outside from the main project)

import requests
URL = "http://127.0.0.1:8000/stuinfo/2"

r = requests.get(url = URL)

data = r.json()

print(data)