    # 1. GUESS A NUMBER

# print("I am thinking of a number between 1 and 10.")
# num = int(input("What's the number?\n"))
# secretNumber = 5

# while (num!=secretNumber):
#     if (num<0 or num>10):
#         print(("Number not in range"))
#         num = int(input("What's the number?\n"))
#     else:
#         print ("Nope, try again.")
#         num = int(input("What's the number?\n"))
# print("Yes! You win!")


    # 2. GIVE HIGH-LOW HINT

# print("I am thinking of a number between 1 and 10.")
# num = ""
# secretNumber = 5

# while (num!=secretNumber):
#     num = int(input("What's the number?\n"))
#     if (num<0 or num>10):
#         print(("Number not in range"))
#     elif (num<secretNumber):
#         print(num,"is too low.")
#     elif (num)>secretNumber:
#         print(num,"is too high.")
# print("Yes! You win!")


    # 3. RANDOMLY GENERATED SECRET NUMBER

# import random
# secretNumber = random.randint(1,10)
# print("I am thinking of a number between 1 and 10.")
# num = ""

# while (num!=secretNumber):
#     num = int(input("What's the number?\n"))
#     if (num<0 or num>10):
#         print(("Number not in range"))
#     elif (num<secretNumber):
#         print(num,"is too low.")
#     elif (num)>secretNumber:
#         print(num,"is too high.")
# print("Yes! You win!")


    # 4. LIMIT NUMBER OF GUESSES

import random
secretNumber = random.randint(1,10)
print("I am thinking of a number between 1 and 10.")
num = ""
guess = 1
# STILL A WIP - did not finish
while (num!=secretNumber):
    num = int(input("What's the number?\n"))
    if (num<0 or num>10):
        print(("Number not in range"))
    elif (num<secretNumber):
        print(num,"is too low.")
    elif (num)>secretNumber:
        print(num,"is too high.")
print("Yes! You win!")

