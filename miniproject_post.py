import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"name": "Jimmy Butch", "net_id": "jjb80", "e-mail": "james.butch@duke.edu"}
r = requests.post(server_name + "student", json=request_json)
print(r.text)
