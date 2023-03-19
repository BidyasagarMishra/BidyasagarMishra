#variables are created outside the function is known as global variable.
#it can be used by everyone and it can be decalre outside as well as inside the function 

print("below are the Example")
x="awesome"
def myfunc():
    print("global variable is "+x)

myfunc()

print("create a variable inside the function and in the same name in globally")
# here we will take the variable as 'x' coz already we have a global variable it will help of us 
def mynewfunction():
    x="very good"
    print("I am "+ x)
    
    
mynewfunction()
print("I am "+ x)

#The global Keyword
#normally when we declare a variable inside the function it is known as local variable. but if we are adding a prefix 'global' keyword then it will be global variable 
print("use of global keyword while declaring a variable")
def myfunctionforgloablkeyeor():
    global y
    y="very bad"
    print("I am "+ y)
    
myfunctionforgloablkeyeor()
print("I am "+ y)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
print("To change the value of a global variable inside a function, refer to the variable by using the global keyword")
d="very bad"
def myfunctionvaluechnageforglobalvariable():
    global d
    d="verybad globally"
    print("I am very bad "+d)

myfunctionvaluechnageforglobalvariable()    
print("I am very bad "+d)
