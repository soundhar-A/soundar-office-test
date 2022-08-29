import requests
from pprint import pprint
import json

headers = {
    "Content-Type":"application/json"
}
data = json.dumps({
    "id":"9",
    "company_name":"sivra",
    "email":"sivra@gmail.com",
    "company_code":"8525",
    "strength":"50",
    "web_site":"https://travellerview.heroku.com"
    
})
reponse = requests.post("http://127.0.0.1:8000/",headers=headers,data=data)
pprint(reponse.text)
