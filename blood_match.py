import requests


server_name1 = "http://vcm-7631.vm.duke.edu:5002/get_patients/jjb80"

r = requests.get(server_name1)
print(r.text)

server_name2 = "http://vcm-7631.vm.duke.edu:5002/get_blood_type/"
donor = requests.get(server_name2+"F6")
recipient = requests.get(server_name2+"M8")
print(donor.text)
print(recipient.text)

if donor.text == recipient.text:
    match = "Yes"
else:
    match = "No"

match_check = {'Name': 'jjb80', 'Match': match}
print(match_check)
server_name3 = "http://vcm-7631.vm.duke.edu:5002/match_check"
r3 = requests.post(server_name3, json=match_check)
print(r3.text)
