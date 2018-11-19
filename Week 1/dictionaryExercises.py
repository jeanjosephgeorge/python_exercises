# phonebook_dict = {
#     "Alice":'703-493--1834',
#     "Bob":"857-384-1234",
#     "Elizabeth":"484-584-2923"
# }
#EXERCISE 1: WRITE CODE TO DO THE FOLLOWING
        
        #1. PRINT ELIZABETH'S PHONE NUMBER

#print (phonebook_dict["Elizabeth"])

        #2. ADD A ENTRY TO THE DICTIONARY: Kareem's number is 938-489-1234

#phonebook_dict["Kareem"] = "938-489-1234"
# print (phonebook_dict)

        #3. DELETE ALICE'S PHONE ENTRY

# del phonebook_dict["Alice"]
# print (phonebook_dict)

        #4. CHANGE BOB'S NUMBER ENTRY to '968-345-2345'

# phonebook_dict["Bob"]="968-345-2345"
# print (phonebook_dict)

        #5. PRINT ALL THE PHONE ENTRIES

# print (phonebook_dict)




# EXERCISE II: NESTED DICTIONARIES

# ramit = {
#     'name':'Ramit',
#     'email':'ramit@gmail.com',
#     'interests':['movies','tennis'],
#     'friends':[
#         {
#             'name':'Jasmine',
#             'email':'jasmine@yahoo.com',
#             'interests':['photography','tennis']
#         },
#         {
#             'name':'Jan',
#             'email':'jan@hotmail.com',
#             'interests':['movies','tv']
#         }
#     ]
# }

        #1. PYTHON EXPRESSION THAT GETS THE EMAIL ADDRESS OF RAMIT

# def ramitemail():
#     print (ramit["email"])

# ramitemail ()

        #2. PYTHON EXPRESSION THAT GETS THE FIRST OF RAMIT'S INTERESTS

# def ramitFirstInterest():
#     print (ramit["interests"][0])

# ramitFirstInterest()

        #3. PYTHON EXPRESSION THAT GETS THE EMAIL ADDRESS OF JASMINE

# def emailJasmine():
#     print (ramit["friends"][0]['email'])

# emailJasmine()

        #4. PYTHON EXPRESSION THAT GETS THE SECOND OF JAN'S TWO INTERESTS

# def Jans2ndInterest():
#     print (ramit["friends"][1]['interests'][1])

# Jans2ndInterest()




# EXERCISE III : LETTER SUMMARY


def letter_histogram():
    word = input("Insert word")
    wordList = []
    for x in word:
        wordList.append(x)
        print (wordList)

letter_histogram()