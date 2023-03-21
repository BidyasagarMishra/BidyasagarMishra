#There are three numeric types in Python: int,float,complex 
x=1 #int
y=2.8 #float
z=1j #complex

print("type of x: ",type(x))
print("type of y: ",type(y))
print("type of z: ",type(z))

#int: is a whole number without decimals and postive or negative
x=1
y=78787865654545
z=-67856
print("type of x: ",type(x))
print("type of y: ",type(y))
print("type of z: ",type(z))

#Float: is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print("type of x: ",type(x))
print("type of y: ",type(y))
print("type of z: ",type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print("type of x: ",type(x))
print("type of y: ",type(y))
print("type of z: ",type(z))

#Complex: are written with a "j" as the imaginary part
x=5j
x=3+5j
z=-5j
print("type of x: ",type(x))
print("type of y: ",type(y))
print("type of z: ",type(z))

#Type Conversion: it is basically known as type casting , convert from one type to anothe type with the int(),float(), and omplex() methods 
x=1
y=1.0
z=1j
a=float(x)
b=int(y)
c=float(x)
print(a)
print(b)
print(c)
print("type of a: ",type(a))
print("type of b: ",type(b))
print("type of c: ",type(c))

#Random Number: Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1, 10))



