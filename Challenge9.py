#Compariosn Game

first = int(input("Enter first number: "))
sec = int(input("Enter second number: "))
ans = input("Are they equal? (yes/no): ")

if first > sec:
    print("First number is bigger")
    answers = (ans == "yes")
    print("Are they equal?", answers)
    
elif first == sec:
    print("Both are equal")
    answers = (ans == "yes")
    print("Are they equal?", answers)
else:
    print("Second number is bigger")
    answers = (ans == "yes")
    print("Are they equal?", answers)