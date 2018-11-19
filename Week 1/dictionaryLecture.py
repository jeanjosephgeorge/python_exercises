# Data type similar to arrays buut works with keys and values instead of indexes.
# Each value stored can accessed using a key, which is any type of object (a string, a number, a list,etc)

# phonebook = {}
# phonebook ["John"] = 2342342
# phonebook ["Jack"] = 2340832
# phonebook ["Jill"] = 1098722

# print (phonebook)

# phonebook = {
#     "Jack":234234234,
#     "John":123123124,
#     "Jill":579247900
# }
#     print (phonebook)

# myContactList = {
#     "first_name":"Jean",
#     "last_name":"George",
#     "age":12,
#     12:"street",
#     "friends":{
#         "first_name": "Oscar",
#         "last_name":"Miranda",
#         "occupation":"student"
#     }
# }

#first_name = myContactList["first_name"]

#first_name = myContactList.get("Dog")
#print(first_name)

# isItThere = "dog" in myContactList
# print(isItThere)

# if ("last_name" in myContactList):
#     print(myContactList["last_name"])

# myList=["one","two","three"]
# myList[0] = 1
# print(myList)

#print(myContactList.keys())
#print(myContactList.values())

# del myContactList[12]
# print (myContactList.keys())

                    #ITERATING OVER VALUES IN DICTIONARY

# for key, value in myContactList.items():
#     #print(value)
#     print("{key},{value}".format(key=key,value=value))

contactList = [
    {"first_name":"Veronica",
    "last_name":"Lino",
    "email":"vernica@dc.com",
    "phone":{
        "home":"222-222-2222",
        "cell":"333-333-3333"
    }
    },
    {"first_name":"Jean",
    "last_name":"George",
    "email":"jean.joseph@outlook.com",
    "phone":{
        "home":"444-444-4444",
        "cell":"555-555-5555"
    }
    },
    {"first_name":"Jim",
    "last_name":"Joseph",
    "email":"jimjose@outlook.com",
    "phone":{
        "home":"666-666-6666",
        "cell":"777-777-7777"
        }}
]
#How to get Veronica's email?
result = contactList[0]["phone"]["cell"]
print(result)
