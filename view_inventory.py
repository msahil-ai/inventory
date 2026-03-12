from ensure_storage import load_file

def load_data_table(arg:str,threshold):

    data=load_file(arg)

    if data is None:
        print("Inventory is empty. Please add items first.")
        exit()

    else:
        for i in data:
            if i["Quantity"]<=threshold:
                i["Quantity"]=str(i["Quantity"])+" *** LOW STOCK ***"
            res = i.__str__() 
            res = res.replace('{', '').replace('}', '').replace("'",'')
            print(res)
        


if __name__=="__main__":
    load_data_table()