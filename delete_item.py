from ensure_storage import load_file
from ensure_storage import save_file


def delete_item(arg:str):
    
    #PATH="inventory.json"


    id=int(input("Enter the ID of the item you want to delete: "))
    
    data=load_file(arg)
    for i in data:
        if id == i["ID"]:
            sure=input("Are you sure you want to delete this item? (yes/no)")
            if sure=='y' or sure.lower()=='y':
                data.remove(i)
                save_file(data, arg)
                print("Deleted")
                exit()
            if sure=='n' or sure.lower()=='n':
                exit()
    else:
        print(f"ID: {id} not Found!")
           


if __name__=="__main__":
    delete_item()