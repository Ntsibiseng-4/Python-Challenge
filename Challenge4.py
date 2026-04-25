#Work with a list of food

first = input("First item: ")
last = input("Last food: ")

foodList = [first, last]
print(foodList)

#How to insert multiple object using one line
foodList.insert(1,"Burger")
foodList.insert(2,"Sushi")
foodList.insert(3,"Paster")
print(f"Updated list: {foodList}")