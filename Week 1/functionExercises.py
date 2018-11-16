#1.    HELLO FUNCTION

# def name(x):
#     print("Hello,",x,"!")

# name(input("What\'s your name?\n"))


#2.     Y = X+1 Write a function f(x) that returns x + 1 and plot it for x values of -3 to 3 in increments of 1.

import matplotlib.pyplot as plot


# import matplotlib.pyplot as plot

# def f(x):
#     y = x+1
#     return y

# xs = list(range(-3,4))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()


#3.     Square of X:

# import matplotlib.pyplot as plot

# def f(x):
#     y = x*x
#     return y

# xs = list(range(-100,101))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()

#4.     ODD or EVEN as BAR GRAPH!


# import matplotlib.pyplot as plot

# def f(x):
#     if (x%2==0):
#         return (-1)
#     else:
#         return (1)

# xs = list(range(-5,6))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.bar (xs,ys)
# plot.show ()


#5.     SINE FUNCTION

# import matplotlib.pyplot as plot
# import math

# def f(x):
#     y = math.sin(x)
#     return y

# xs = list(range(-5,6))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot (xs,ys)
# plot.show ()


#6.     SINE II FUNCTION

# import matplotlib.pyplot as plot
# import math
# from numpy import arange

# def f(x):
#     y= math.sin(x)
#     return y

# xs = arange(-5,6,0.1)
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot (xs,ys)
# plot.show()


#7.     DEGREE CONVERSION

# import matplotlib.pyplot as plot


# def Cel(x):
#     y=(x*1.8)+32
#     return y

# xs=list(range(0,50))
# ys=[]

# for x in xs:
#     ys.append(Cel(x))

# plot.plot (xs,ys)
# plot.show ()


#8 and 9. PLAY AGAIN

# def play():
#     y = input("Do you want to play again?\n")
#     if (y=="Y" or y=="y"):
#         #return True
#         print ("True")
#         play()
#     elif (y=="N" or y=="n"):
#         #return False
#         print("False")
#     else:
#         print("Invalid input")  
#         play()

# play()
