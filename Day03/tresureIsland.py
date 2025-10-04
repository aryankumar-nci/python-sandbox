print("Welcome to the Treasure Island. Your mission is to find the treasure...")

direction = input("Enter your direction, l or r: \n")
if direction == "r":
    print("Game Over -_-")
else:
    swim = input("Do you want to swim or wait? : s--> swim and w --> wait: \n")
    if swim =="s":
        print("Game Over -_-")
    else:
        door = input("Which door you want? Red: r or Blue: b or Yellow: y\n")
        if door == "y":
            print("Congratulations!!! you win.")
        else:
            print("Game Over -_-")