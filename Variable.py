#python has no command for decalring a variable 
#A variable is created the moment you first assign a value to it 
x=5
y="Bidyasagar"
print(x)
print(y)

a=5 #here a is int type
a="Bidya" #here a is string type
print(a); # here it will print the value of 'a' as "Bidya" coz this one is the latest one declared


#Casting
print("Casting started from here")
x=str(3) #x will be '3'
y=int(3) #x will be 3
z=float(3) #x will be 3.0
print(x)
print(y)
print(z)

#Get the type
print("Get the type started from here")
print(type(x))
print(type(y))
print(type(z))

print("Get the type started from here")
x="x is double quote string"
y="y is single quote string"
print(x,y,"but there is no differences")

#Case-Sensitive
print("Case-Sensitive started from here")
a="Bidya"
A="Sagar"
#both will be different variables, we can create different datatype as well 
print(a,A)
print("A will not overwrite a")