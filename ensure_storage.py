import os.path
import json

#PATH="inventory.json"

def ensure_file(path:str): #create file
    if os.path.exists(path)==False:
        with open(path, "x") as f1:
            task={"task":[]}
            json.dump(task, f1)
    try:
        with open(path,"r") as f: 
            data=json.load(f)
            
    except json.JSONDecodeError:
        with open(path, "w") as d:
            task={"task":[]}
            json.dump(task, d)
        


def load_file(arg:str):
    temp_list=[] #inventory view
    with open(arg, "r") as f:
        f1=json.load(f)
    for i in f1.get("task"):
        temp_list.append(i)
    #print(temp_list)
    return temp_list #this data will be sent to view_inventory

def save_file(data:list, p:str):
    with open("inventory.json", "w") as f:
        #dict['task']=json.dump(data, f)
        #f.update({"task": data})
        r={"task":data}
        json.dump(r, f)
        #json.dump("\n", f)



if __name__=="__main__":
    #load_file(path)
    ensure_file(PATH)