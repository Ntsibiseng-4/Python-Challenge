#Age checker

age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult!")
elif age >= 13 or age <= 18:
    print("You are teen!")
else:
    print("You are a child!")