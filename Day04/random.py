import random

choice = input("choose head or tail: h or t....\n")

coin = random.randint(1,10)
if coin<=5 and choice=="h":
    print("head..you win")
elif coin<=10 and choice =="t":
    print("tails..you win")
else:
    print(f"{coin}...you lose")
