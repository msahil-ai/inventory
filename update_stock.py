from ensure_storage import load_file
from ensure_storage import save_file


def update_item(arg:str):
    
    #PATH="inventory.json"


    id=int(input("Enter the ID of the item you want to update: "))
    
    data=load_file(arg)
    for i in data:
        if id == i["ID"]:
            print(i)
            sure=input("Are you sure you want to update this item? (yes/no)")
            if sure=='y' or sure.lower()=='y':
                op=int(input("Operation: (1) Sell (2) Restock:\t"))
                quantity=int(input("Enter Quantity: "))
                if op==1:
                    if i["Quantity"]>=quantity:
                        i["Quantity"]=i["Quantity"]-quantity
                        save_file(data, arg)
                        print(f"Stock updated remaining stock for {i['ID']} is:\t {i['Quantity']}")
                    else:
                        print(f"Error: Insufficient stock. Only {i['Quantity']} units available.")
                elif op==2:
                    i["Quantity"]=i["Quantity"]+quantity
                    save_file(data, arg)
                    print(f"Stock updated. New quantity for ITEM: {i['Quantity']}")
                else:
                    print(" You Entered Wrong Choice!!")
                    exit()
                
            if sure=='n' or sure.lower()=='n':
                exit()

if __name__=="__main__":
    update_item()