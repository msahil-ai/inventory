import os.path
import json

path="inventory.jsonl"

def ensure_file(): #create file
    if os.path.exists(path)==False:
        f1=open("inventory.jsonl", "x")
    else:
        print("file already exists!")

def load_file(): #inventory view
    f1=open("inventory.jsonl", "r")
    data=f1.read()
    return data #this data will be sent to view_inventory

def save_file(data):
    f1=open("inventory.jsonl", "a")
    f1.write(json.dumps(data))
    f1.write(",")
    f1.write("\n")
    f1.close()


if __name__=="__main__":
    ensure_file()