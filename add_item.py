#add new item structure
import json
#from ensure_storage import is_file

def add_item():
    count=0
    item_list=[]
    


    while True:
        #with open('inventory.json') as f:


        item_data={}  #dictonary name is fixed so that is why the data is getting updated in the same dictionary and not creating a new one. if we create a new one then it will be added to the list and we will get the desired output.

        item_data["ID"]=count+1
        item_data["Name"]=input("Please Enter the Name of the item:\t ")
        item_data["Price"]=float(input("Please Enter the Price of the item:\t "))
        item_data["Quantity"]=float(input("Please Enter the Quantity of the item:\t "))
        item_data["Category"]=input("Please Enter the Category of the item:\t ")
        item_list.append(item_data)
        print("ITEM" , item_data["Name"] ,"ADDED SUCCESSFULLY WITH ID: ", item_data["ID"])
        count+=1

        con=input("Do you want to add more?y/n\t")
        if con =='y' or con.lower()=='y':
            continue
        elif con == 'n' or con.lower()=='n':
            break
        else:
            print("Invalid input! Try again.")

    print(item_list)
    return item_list
    #f= open("./inventory.json", 'w')
    #f.write(json.dumps(item_list))
    #f.close()
    
    
if __name__=="__main__":
    add_item()


