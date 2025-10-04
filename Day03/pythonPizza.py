print("Welcome to the Python Pizza Deliveries!")

bill =0
size = input("Enter the size of pizza. S,M,L: ")
pepperoni = input("Do you  want pepperoni on pizza? yes: y, No: n")
cheese = input("Do you want some extra cheese? y or n")
if size=="S":
    bill = 15

elif size =="M":
    bill =20

elif size =="L":
    bill =25

else:
    print("You choose wrong option.")

if pepperoni =="Y":
    if size =="S":
        bill +=2
    else:
        bill +=3


if cheese == 'y':
    bill += 1




print(f"Your final bill is ${bill}")