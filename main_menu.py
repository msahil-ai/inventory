from add_item import add_item
from search_item import search_item
from view_inventory import load_data_table
from summary import show_summary
from delete_item import delete_item
from update_stock import update_item
PATH='inventory.json'

print("=======STOCKMASTER=======")
print("1.Add New Item")
print("2.View All Inventory")
print("3.Search Item")
print("4.Update Stock (Sell/Restock)")
print("5.Delete Item")
print("6.Show Summary")
print("7.Exit")
print("="*25)

choice = int(input("Enter your choice: "))

if choice == 1:
    add_item(PATH)
elif choice == 2:
    print("Viewing all inventory...")
    load_data_table(PATH)
elif choice == 3:
    print("Searching items....")
    search_item(PATH)
elif choice == 4:
    update_item(PATH)
elif choice == 5:
    delete_item(PATH)
elif choice ==6:
    show_summary(PATH)
elif choice ==7:
    exit()
else:
    print("Invalid Input!")
    exit()