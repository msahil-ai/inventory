import requests
import json
from ensure_storage import load_file

def search_item(arg:str):

    search=int(input("Search by (1) Name or (2) ID?"))
    if search==1:
        name=input("Enter the name of the item you want to search for: ")
        name_result=[]
        data=load_file(arg)
        for i in data:
            if name in i["Name"]:
                name_result.append(i)
        print(name_result)

    elif search==2:
        id=int(input("Enter the ID of the item you want to search for: "))
        id_result=[]
        data=load_file(arg)
        for s in data:
            if id == s["ID"]:
                id_result.append(s)
                break
        print(id_result)

    else:
        print("Invalid input. Please enter 1 or 2.")            


if __name__=="__main__":
    search_item()