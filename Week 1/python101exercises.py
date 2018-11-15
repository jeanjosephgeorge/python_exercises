#         # 1. Hello, you!

# name = input ("What is your name?\n")
# print ("Hello "+name+"!")

#         #2. HELLO, YOU!

# name = input("What is your name?\n")
# print ("HELLO "+name.upper()+". YOUR NAME HAS "+ str(len(name)) + " LETTERS IN IT! AWESOME")

#         #3. Madlib

# name = input("Please fill in the blanks:\n____(name)____\'s favorite subject in school is ____(subject)____.\nWhat is name?\n") 
# subject = input("What is subject?\n")
# print (name+"\'s favorite subject in school is "+subject)

#         #4. Day of the Week

# day = int(input('Day (0-6)? '))
# week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# if day<=6:
#    print (week[day])
# else:
#    print ("Invalid selection")

#         #5. Work or Sleep in?

# day = int(input('Day (0-6)? '))
# week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# if day == 0:
#    print ("Sleep in.")
# elif day == 6:
#     print ("Sleep in.")
# elif day>=7:
#    print ("Invalid selection")
# else:
#     print ("Go to work.")

#         #6. Celsius to Fahrenheit

# temp = int(input("Temperature in Celsius?\n"))
# print ((temp*1.8)+32)

#         #7. Tip Calculator

# bill = int(input("What is the bill amount?\n"))
# level = input("Level of service? Good, Bad or Fair?\n")
# if level == "good":
#     tip = round((0.2*bill),2)
#     print("Tip amount: $",tip)
# if level == "fair":
#     tip = round((0.15*bill),2)
#     print("Tip amount: $",tip)
# if level == "bad":
#     tip = round((0.1*bill),2)
#     print("Tip amount: $",tip)

# print ("Total amount: $", round((bill+tip),2))

#         #8. Tip Calculator 2

# bill = int(input("What is the bill amount?\n"))
# level = input("Level of service?\nWas it good, bad or fair?\n")
# split = int(input("Split how many ways?\n"))
# if level == "good":
#     tip = round((0.2*bill),2)
#     print("Tip amount: $",tip)
# if level == "fair":
#     tip = round((0.15*bill),2)
#     print("Tip amount: $",tip)
# if level == "bad":
#     tip = round((0.1*bill),2)
#     print("Tip amount: $",tip)

# print ("Total amount: $", round((bill+tip),2))
# print ("Amount per person: $",round((bill+tip)/split,2))

#         #9. 1 to 10

# count = 0
# while count<=10:
#     print (count)
#     count+=1 

#10. How many coins?

coins = 0
while (input("You have "+str(coins)+" coins.\nDo you want another?\n") == "yes"):
    coins+=1
print ("Bye")