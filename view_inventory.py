from ensure_storage import load_file

PATH="inventory.json"


def load_data_table():

    data=load_file(PATH)

    if data is None:
        print("Inventory is empty. Please add items first.")
        exit()

    else:
    
        print(data)
        #print(00)

