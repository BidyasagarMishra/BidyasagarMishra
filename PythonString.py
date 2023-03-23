#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is same as "hello"
x="Hello double quotation"
y='Single quotation'
print(x)
print(y)


#multiline string declaration using double quotationfor
a="""Hello Bidya,

I hope you are continuing with python programing and you are using  double quotationfor the multi line string

Regards
Bidyasagar"""
print(a);


#multiline string declaration using single quotationfor
b='''Hello Bidya,

I hope you are continuing with python programing and you are using  single quotationfor the multi line string

Regards
Bidyasagar'''
print(b);

#strings are arrays
#like other programing python does not have the character data type, a single character is simply a string with a length of 1.
#square brackets can be used to access elements of the string 
a="Hello, world"
print(a[0])

#looping through a string 
for letter in "banana":
    print(letter)
    
#length of string
a="hellow, world"
print(len(a))

#check string(in): here we will check a particular character or string in python if that exists or not in the whole string if exists then return true else false.
txtval="I am the best among my friends"
print("best" in txtval)

#check string(in), using if condition
txtval="I am the best among my friends"
if "best" in txtval:
    print("yes, 'best' is available in ",txtval)
    
    
#check string(not in): here we will check a particular character or string in python if that not exists in the whole string if not exists then return true else false.       
txtval="I am the best among my friends"
print("I am milan" not in txtval)

#check string(not in), using if condition
txtval="I am the best among my friends"
if "I am milan" not in txtval:
    print("No, 'I am milan' is not present in ",txtval)