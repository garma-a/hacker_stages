import random
num = int(input("choice number from 1 to 10 plz : "))
if num > 10:
    print("number is greater than 10")
elif num < 1:
    print("number is less than 1")
rand_num = random.randint(1, 10)
if num == rand_num:
    print("you win!")
else:
    print("you lose the random number was " , rand_num);

