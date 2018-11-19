#1. CONVERT STRING TO UPPERCASE
 
# oldLine = input("What would you like to convert to uppercase?\n")

# newLine=oldLine.upper()
# print(newLine)



#2. CONVERT STRING TO LOWERCASE

# oldLine = input("What would you like to convert to lowercase?\n")

# newLine=oldLine.lower()
# print(newLine)



#3. REVERSE A STRING

# oldLine = input("String you would like to reverse?\n")

# newLine = oldLine[::-1]
# print (newLine)


#**** OR using a FOR loop *****


# oldLine = input("String to reverse\n")
# oldArray = []
# newArray = []
# newLine = ""

# for x in oldLine:
#     oldArray.append(x)

# for r in range(0,len(oldArray)):
#     word=oldArray[(len(oldArray)-1-r)]
#     newArray.append(word)

# newLine = ''.join(newArray)
# print (newLine)



#4. Leetspeak

# oldLine = input("Input line to be converted into Leetspeak\n")
# oldLineU = oldLine.upper()
# newList=[]
# newLine=""

# for x in oldLineU:
#     if x=="A":
#         x= "4"
#     if x=="E":
#         x= "3"
#     if x=="G":
#         x= "6"
#     if x=="I":
#         x= "1"
#     if x=="O":
#         x= "0"
#     if x=="S":
#         x= "5"
#     if x=="T":
#         x= "7"
#     newList.append(x)

# newLine = ''.join(newList)      # had to google how to join list to convert into string
# print(str(newLine))



#5. LONG-LONG VOWELS

# oldLine = (input("Input sentence you'd like to long-vowelify\n"))
# oldList = []
# newList = []
# newLine = ""

# for x in oldLine:
#     oldList.append(x)

# for i in range(0,(len(oldList))):
#     if (oldList[i-1] == "o" and oldList[i-1] == oldList[i]): # Did not create for a,i and u as most words dont have them
#         oldList[i]="oooo"
#     if (oldList[i-1] == "e" and oldList[i-1] == oldList[i]):
#         oldList[i]="eeee"
#     newList.append(oldList[i])

# newLine = ''.join(newList)
# print (newLine)


#6. CAESAR CIPHER:

from pycipher import CAESAR

# oldLine = input ("Insert text to cipher")
# oldList = []

# for x in oldLine:
#     oldList.append(x)

caesar(key=13).decipher("lbh zhfg hayrnea jung lbh unir yrnearq")