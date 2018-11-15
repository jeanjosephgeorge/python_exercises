    # 1. SUM THE NUMBERS

# list1 = [2,3,7,9,13]
# total=0

# for x in list1:
#     total+=x
# print ("Sum total is",total)


    # 2. LARGEST NUMBERS

# list1 = [32,74,21,65,44]

# list1.sort()
# last = int(len(list1))
# print ("Largest number in the string is",(list1[len(list1)-1]))


    # 3. SMALLEST NUMBERS

# list1 = [34,67,23,11,87,43]

# list1.sort()
# print("Smallest number in the string is",list1[0])


    #4. EVEN NUMBERS

# list1 = [12,33,57,54,90,21]

# for x in list1:
#     if x%2 == 0:
#         print (x)


    #5. POSITIVE NUMBERS

# list1 = [23,-31,54,-6,10,29,-23]

# for x in list1:
#     if x>=0:
#         print (x)

    
    #6. POSITIVE NUMBERS II


# list1 = [23,-31,54,-6,10,29,-23]
# list2 = []

# for x in list1:
#     if x>=0:
#         list2.append(x)
# print (list2)


    #7. MULTIPLY A LIST

# list1 = [23,31,54,6,10,29,23]
# factor = 2
# list2 = []

# for x in list1:
#     new=(x*factor)
#     list2.append(new)
# print(list2)


    #8. MULTIPLY VECTORS

# list1 = [2,4,5]
# list2 = [2,3,6]
# list3 = []

# for i in range(0,3): 
#     l3 =list1[i] * list2[i]
#     list3.append(l3)
# print (list3)


    #9. MATRIX ADDIION

# list1 = [1,3,2,4]
# list2 = [5,2,1,0]
# list3 = []

# for i in range(0,(len(list1))): 
#     l3 =list1[i] + list2[i]
#     list3.append(l3)
# print (list3)


    #10. MATRIX ADDITION II

# list1 = [1,3,2,4]
# list2 = [5,2,1,0]
# list3 = []

# if len(list1) != len(list2):
#     print ("This cannot be added. Check your lists.")
# else:
#     for i in range(0,(len(list1))): 
#         l3 =list1[i] + list2[i]
#         list3.append(l3)
#     print (list3)

    #11. DE-DUP

# list1 = [2,3,3,5,7,7,8,4,1,1]
# uniqList = []

# for x in list1:
#     if x not in uniqList:       #Had to google this bit
#         uniqList.append(x)

# print (uniqList)


    #12. BONUS - MULTIPLYING MATRICES