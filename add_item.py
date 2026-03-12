import json
import os
from ensure_storage import ensure_file, save_file, load_file
import datetime

def add_item(arg:str):

    ensure_file(arg)

    if os.path.exists("id_value.txt"):
        with open("id_value.txt", "r") as file:
            id = int(file.read())
    else:
        id=1000
        
    PATH=arg
    item_list=[]
    count=1


    while True:

        item_data={}  #dictonary name is fixed so that is why the data is getting updated in the same dictionary and not creating a new one. if we create a new one then it will be added to the list and we will get the desired output.

        item_data["ID"]=id+1
        item_data["Name"]=input("Please Enter the Name of the item:\t ")
        item_data["Price"]=float(input("Please Enter the Price of the item:\t "))
        item_data["Quantity"]=float(input("Please Enter the Quantity of the item:\t "))
        item_data["Category"]=input("Please Enter the Category of the item:\t ")
        item_list.append(item_data)
        print("ITEM" , item_data["Name"] ,"ADDED SUCCESSFULLY WITH ID: ", item_data["ID"],"at", datetime.datetime.now().replace(microsecond=0))
        count+=1
        id+=1

        con=input("Do you want to add more?y/n\t")
        if con =='y' or con.lower()=='y':
            data=load_file(PATH)#.get('task')
            print(f"[DEBUG] {data}")
            data.append(item_data)
            #data.update(item_list)
            save_file(data, PATH) #
            continue
        elif con == 'n' or con.lower()=='n':
            data=load_file(PATH)#.get('task')
            print(f"[DEBUG] {data}")
            data.append(item_data)
            #data.update({"task":item_list})
            save_file(data, PATH) #
            break
        else:
            print("Invalid input! Try again.")

    print(item_list)
    #save_file(item_data)
    file=open("id_value.txt", "w")
    file.write(str(id))
    file.close()


    return item_list
    
    
    
if __name__=="__main__":
    add_item()

