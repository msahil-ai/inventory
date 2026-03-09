import os.path
import json

path="inventory.json"

def ensure_file(): #create file
    if os.path.exists(path)==False:
        f1=open("inventory.json", "x")
    else:
        print("file already exists!")

def load_file(): #inventory view
    f1=open("inventory.json", "r")
    data=f1.read()
    return data #this data will be sent to view_inventory

def save_file(data):
    f1=open("inventory.json", "a")
    f1.write("\n")
    f1.write(data)


if __name__=="__main__":
    ensure_file()