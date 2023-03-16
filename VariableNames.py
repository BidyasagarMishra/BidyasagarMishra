"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""

#legal variable names
myVar="Sunday"
MyVar="Monday"
_MyVar="Tuesday"
_myVar="Wednesday"
_myvar="Thursday"
_MYVAR="Friday"
_myVaR="Saturday"

print("-------------Legal Variable Names-------------------")
print(myVar)
print(MyVar)
print(_MyVar)
print(_myVar)
print(_myvar)
print(_MYVAR)
print(_myVaR)

print("-------------Camel case Variable Names-------------------")
myCamelCase="Camel case Variable"
print(myCamelCase)

print("-------------Pascal case Variable Names-------------------")
MyPascalCase="Pascal case Variable"
print(MyPascalCase)

print("-------------Snake case Variable Names-------------------")
my_SnakeCase="Snake case Variable"
print(my_SnakeCase)



