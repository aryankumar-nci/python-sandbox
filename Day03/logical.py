print("Welcome to the event ride....")
height = int(input("What is your height?: "))

bill=0

if height>120:
    print("You can ride.")
    age=int(input("Enter your age here."))
    if age<=12:
        print("Pay $5")
        bill=5
    elif age<=18:
        print("Pay $7.")
        bill=7
    elif age>=45 and age <=50:
        print("Everything is gonna be OK..YOUR RIDE IS FREE")
    else:
        print("Pay $12")
        bill=12
    photo=input("Do you want a photo take? type y for yes and n for no.")
    if photo =="y":
        bill = bill +3

    print(f"your final bill is {bill}")



else:
    print("you are too short for this.")