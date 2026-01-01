print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("Do you want to take a photo? (y/n) ")

if height >= 120:
    if age < 12:
        ticket = 5
    elif 12 <= age <= 18:
        ticket = 7
    else:
        ticket = 12
    if photo == "y":
        ticket += 3
    else:
        ticket += 0
    print(f"You can ride the rollercoaster! The ticket is ${ticket}")
else:
    print("You can not ride the rollercoaster!")
