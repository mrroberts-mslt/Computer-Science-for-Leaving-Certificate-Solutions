shopping_list = []

print("Enter items for your shopping list.")
print("Type 'remove' to delete an item, or 'done' to finish.")

item = ""  # initialise variable before loop

while item != "done":
    item = input("Enter item: ").lower()

    if item == "done":
        break
    elif item == "remove":
        remove_item = input("Which item would you like to remove? ").lower()
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(remove_item, "removed.")
        else:
            print(remove_item, "is not in the list.")
    else:
        shopping_list.append(item)
        print(item, "added.")

print("\nYour final shopping list:")
print(shopping_list)
print("Total items:", len(shopping_list))

if "milk" in shopping_list:
    print("You have milk on your list.")
else:
    print("You don't have milk on your list.")
