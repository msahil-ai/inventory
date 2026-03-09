from item_structure import add_item

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