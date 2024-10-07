print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!Welcome to bus ticket booking system!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")

bus_ticket = ["Vellore", "Arcot", "Kaveripakkam", "Chennai"]
name = input("Enter your name: ")
phone = input("Enter your phone number: ")
print("Hi sir, my bus ticket booking system is ready to help you book your bus tickets.")
print(f"My name is {name}, and your number is {phone}.\n")
print("Sure sir, I can help you book your bus tickets for the following bus routes. You can see bus stops and timings from the below links:\n")
print(bus_ticket)

source = input("Enter your source city: ")
destination = input("Enter your destination city: ")
data = input("Enter your travel date and time in the format of DD/MM/YYYY HH:MM AM/PM: ")
seats = input("How many seats do you want to book? ")

choice_book = input("Do you want to proceed with the booking? (y/n): ")

if choice_book.lower() == "y":
    print("Sure sir, I will proceed with the booking.\n")
    print(f"Sure sir, I will book your bus ticket from {source} to {destination} on {data}.\n")
    print(f"Sure sir, I will book {seats} seat(s).\n")
    print("Thank you sir for using my bus ticket booking system.")
else:
    print("Sure sir, I will not process the booking request.\n")

traver_bus = input("Sir, can you show your ticket to me? (y/n): ")

if traver_bus.lower() == "y":
    print("Sure sir, I will show my bus ticket to you.\n")
    print(f"This is my bus ticket for the route, {source} to {destination} on {data}.\n")
    print("Thank you for showing me your bus ticket.")
else:
    print("Sure sir, I will not show my bus ticket to you.\n")    

