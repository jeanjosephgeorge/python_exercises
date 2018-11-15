    #1. FROM 1 to 10

# for x in range(1,11):
#     print (x)


    #2. N TO M

# x = int(input("What number would you like to start from?\n"))
# y = int(input("What number would you like to end at?\n"))
# if y>x:
#     for x in range(x,y):
#         print(x)
# else:
#     print("Invalid range.")


    #3. ODD NUMBERS

# for x in range(1,10):
#     if x%2!=0:
#         print (x)


    #4. PRINT A SQUARE

# length ="x"*5
# for x in range (0,5):
#     print (length)


    #5. PRINT A SQUARE OF N SIZE / SQUARE II

# size = int(input("What size would you like your square to be?\n"))
# length = 'x'*size
# for x in range (0,size):
#     print (length)


    #6. PRINT A BOX

# x = int(input("What height would you like your box to be?\n"))
# y = int(input("What width would you like your box to be?\n"))
# length="x"*y

# print (length)
# for i in range (x-2):
#     print("x"+(" "*(y-2))+"x")
# print (length)


    #7. PRINT A TRIANGLE

# i="*"
# j=5
# for x in range (1,8,2):
#     print (" "*j+i*x)
#     j=j-1


    #8. PRINT A TRIANGLE OF N SIZE

# x = int(input("What height triangle would you like?"))
# i="*"
# j=x
# for x in range (1,(x*2),2):
#     print ((j*" "),(i*x))
#     j=j-1


    #9. MULTIPLICATION TABLE

# for x in range (1,11):
#     for y in range (1,11):
#         print(x,"x",y,"=",(x*y))


    #10. PRINT A BANNER

# text = input("What text would you like to insert?\n")
# length=len(text)

# print("*"*(length+4))
# print("* "+text+" *")
# print("*"*(length+4))

