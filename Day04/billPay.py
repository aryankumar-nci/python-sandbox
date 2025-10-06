
import random
friends = ["Alice","Bob","Charlie","David","Emily"]

#approach 1
person_pay = random.choice(friends)
print(f"{person_pay} will pay the bill.")

#approach 2

person_pay2 = random.randint(0,4)
person = friends[person_pay2]
print(f"{person} will pay the bill this time.")