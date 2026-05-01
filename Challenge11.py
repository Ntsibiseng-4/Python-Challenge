#Shopping List Manager

Intial_list = ["Milk", "Bread", "Eggs"]

add = input("Add an item: ")  #Adding item at the end
Intial_list.append(add)
print(Intial_list)

removing = input("Remove item: ")  #Removing items
Intial_list.remove(removing)
print(Intial_list)

inserting = input("Inserting an item: ")  #Adding item with index
Intial_list.insert(1, inserting)
print(Intial_list)

idx = input('Enter an item: ')  #Getting an index
print(Intial_list.index(idx))


length = len(Intial_list)  #Getting the length
print(f"The length is {length}")