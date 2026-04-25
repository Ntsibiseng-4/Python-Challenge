#Working with Dictionary store and update contact details

name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")

contact = {"Name" : name, "Phone" : phone, "Email" : email}
print(contact)

location = input("Enter your location: ")

contact["Location"] = location
print("Full Contact: ", contact)