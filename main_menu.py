from add_item import add_item
from search_item import search
from view_inventory import load_data_table

print("=======STOCKMASTER=======")
print("1.Add New Item")
print("2.View All Inventory")
print("3.Search Item")
print("4.Update Stock (Sell/Restock)")
print("5.Delete Item")
print("6.Show Summary")
print("7.Exit")
print("="*25)

choice = input("Enter your choice: ")

if choice == '1':
    add_item()
elif choice == '2':
    print("Viewing all inventory...")
    load_data_table()
elif choice =='3':
    print("Searching items....")
    search()
