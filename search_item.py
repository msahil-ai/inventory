import requests

def search(search):

    ans=[]

    print("Search by (1) Name or (2) ID?")
    data=requests.get("inventory.json").json 

    for i,j in data.items():
        if search in j:
            ans.append(i)
