# PHONEBOOK APP

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit

phonebook = {
    'Jean':'123-163-6525',
    'Jim':'934-463-5651',
    'Tom':'854-345-2542'
}

#1. Look up an entry
def lookUp():
    name=str(input("Name:\n"))
    number=phonebook[name]
    print("Found entry for "+name+": "+number+"\n")
    mainMenu()

#2. Set an entry
def setUpEntry():
    name=str(input("Name:\n"))
    number=str(input("Phone Number\n"))
    phonebook[name]=number
    print("Entry stored for "+name+".\n")
    mainMenu()

#3. Delete an entry
def deleteEntry():
    name=str(input("Name:\n"))
    del phonebook[name]
    print ("Deleted entry for "+name+"\n")
    mainMenu()

#4. List all entries
def listAll():
    print(phonebook)
    mainMenu()


#Create Menu
def mainMenu():
    print("Electronic Phone Book\n=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")
    option=int(input("What do you want to do (1-5)?\n"))
    if option==1:
        print(lookUp())
    elif option==2:
        print(setUpEntry())
    elif option==3:
        print(deleteEntry())
    elif option==4:
        print(listAll())
    elif option==5:
        print("Bye")
        quit()
    else:
        print("Invalid selection!\n")
        mainMenu()

#Call Menu
mainMenu()
