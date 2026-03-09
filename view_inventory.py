from ensure_storage import load_file

def load_data_table():

    if "inventory.jsonl" is None:
        print("Inventory is empty. Please add items first.")
        exit()

    else:
        data=load_file()
        print(data)

