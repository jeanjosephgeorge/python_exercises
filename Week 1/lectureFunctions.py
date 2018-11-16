# def sampleFunction():
#     print("Hello World")
# sampleFunction()

# def f(x):
#     print(x)

# f("DigitalCraft")

# def f(x):
#     return x*x

    # myFunctionCall = f(4)       # In this block, we assign a function to a variable
    # print (myFunctionCall)

#  HERE WE CREATE FUNCTIONS, CALL THEM AND THEN USING THE FORMAT FUNCTION, CREATE A TABLE-ISH THING

# def f(x):
#     return x*x

# def g(x):
#     return x+1

# for index in range (-3,5):
#     print("f({x})={y}\t\tg({x})={z}".format(x=index, y=f(index),z=g(index)))


# ARGUMENTS AND KEYWORD ARGUMENTS

# def sampleFunction(a,b,c):
#     print("{a} {b} {c}".format(a=a,b=b,c=c))

# sampleFunction(c=1,a=2,b=3)

# from math import sqrt

# def quadratic(a,b,c):
#     x1 = (-b / (2*a))
#     x2 = (sqrt(b**2 - 4*a*c) / (2*a))
#     return (x1+x2),(x1-x2)

# print (quadratic(31,93,62))


# GLOBAL AND LOCAL VARIABLE

# a = [1,2,3,4,5]

# def someFunction():
#    a[0]=23
#    print("Inside function is {a}".format(a=a))

# print ("Outside function {a}".format(a=a))

# someFunction()

#------------------------

# a = [1,2,3,4,5]

# def someFunction():
#     newArray=a.copy()   # Here we make a copy of the Array A, else it changes it on the global scale even if it is in the local
#     newArray[0]=234
#     print(newArray)

# someFunction()
# print (a)

# MATPLOTLIB

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# xrange = list(range(2,10))
# yrange = list(range(2,10))

# pyplot.plot (xrange,yrange)

# pyplot.savefig('samplePlot.png')

# # pyplot.close()
# __________________________THIS WORKS

# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot

# f_output=[]
# g_output=[]

# def f(x):
#     return 2*x+1

# def g(x):
#     return x+1

# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))

# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close()

#________________TURTLE GRAPHICS!!___________

# from turtle import *

# pencolor('orange')
# width(7)
# circle(180)
# # move into position

# up()
# forward(50)
# left(90)
# forward(50)
# left(90)
# down()

# # draw the square
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# mainloop()

#CONVERTING LIST MULTIPLACTION INTO FUNCTION 

def determinant(l1,l2,l3):
    

    for indexList1 in list1 :

    list3SummedValue = 0
    print("list 1 index: {}".format(indexList1))
    for indexList2 in list2:
       list3SummedValue += indexList1 * indexList2
       print("accumulatedValue {}".format(list3SummedValue))

   list3.append(list3SummedValue)

list1 = [1,5,3,6,7]

list2 = [3,6,9,10,2]

list3 = []

print(list3)