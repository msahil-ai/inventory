from ensure_storage import load_file

def show_summary(path:str):
    data=load_file(path)
    unique_category=set()
    total_items=set()
    break_down={}
    total_units=0
    total_value=0.0
    count=0
    for i in data:
        total_units+=i["Quantity"] #total units in inventory
        total_value+=i["Quantity"]*i["Price"] #total inventory value
        if i["Name"] not in total_items:
            total_items.add(i["Name"])
            count+=1 #count total number of unique products
        if i["Category"] not in unique_category:
            unique_category.add(i["Category"]) #list(set) of unique categories
    sum=0
    for j in unique_category:
        for i in data:
            if j==i["Category"]:
                sum+=i["Quantity"]
            break_down[j]=sum
            

    print(f"The count of distinct item types are:\t {count}")
    print(f"The sum of all quantities is:\t {total_units}")
    print(f"The sum of (Quantity * Price) for all items:\t {total_value}")
    print(f"Category Breakdown: \n{break_down}")

if __name__=="__main__":
    show_summary()        
        

