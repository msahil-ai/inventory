import requests

def search():

    ans=[]

    search=int(input("Search by (1) Name or (2) ID?"))
    if search==1:
        name=input("Enter the name of the item you want to search for: ")
        name_result=[]
        with open("inventory.jsonl", "r") as data:
            for name in data:
                name_result.append(name_result)
            print(name_result)
    elif search==2:
        id=int(input("Enter the ID of the item you want to search for: "))
        id_result=[]
        with open("inventory.jsonl", "r") as data:
            for id in data:
                id_result.append(id_result)
            print(id_result)
    else:
        print("Invalid input. Please enter 1 or 2.")            


if __name__=="__main__":
    search()