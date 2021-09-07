# let assume this is third party application(can be of android , java.....)

import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"



# to read data from database, request to api
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)

    data = r.json()

    print(data)

# get_data()





# for create data in database, request to api
def post_data():
    data = {
        'name':'Rohan',
        'roll': 124,
        'city':'Bokaro'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

post_data()


# for update(this is update fully using put) in database, request to api
def update_data():
    data = {
        'id' : 5,
        'name':'Kunal',
        'city':'Ranchi'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()




# for delete, data from database, request to api
def delete_data():
    data = { 'id' : 5 }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()