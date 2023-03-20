#Built-in Data Types
"""In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:"""
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

print("Getting the datatype")
x=5
print(type(x))

print("Setting the datatype")

print("str datatype")
a="Hi Bidya"
print(a)

print("int datatype")
b=5
print(b)

print("float datatype")
c=20.5
print(c)

print("complex datatype")
d="ij"
print(d)

print("list datatype")
e=["apple","banana","kakudi"]
print(e)

print("tupple datatype")
f=("apple","banana","kakudi")
print(f)

print("range datatype")
g=range(5)
print(g)

print("dict datatype")
h={"name" : "John", "age" : 36}
print(h)

print("set datatype")
h={"apple", "banana", "cherry"}
print(h)

print("frozenset datatype")
i=frozenset({"apple", "banana", "cherry"})
print(i)

print("bool datatype")
j=True
print(j)

print("bytes datatype")
l=b"hello"
print(l)

print("bytearray datatype")
m=bytearray(5)
print(m)

print("memoryview datatype")
n=memoryview(bytes(5))
print(n)

print("NoneType datatype")
o=None
print(x)

#Setting the Specific Data Type, it is kind of typecasting
print("Setting the Specific Data Type | it's kind of type casting")

x=str("Hello world")
print(x)

x=int(20)
print(x)

x=float(20.5)
print(x)

x=complex(1j)
print(x)

x=list(("apple", "banana", "cherry"))
print(x)

x=tuple(("apple", "banana", "cherry"))
print(x)

x=range(6)
print(x)

x=dict(name="John", age=36)
print(x)

x=set(("apple", "banana", "cherry"))
print(x)

x=frozenset(("apple", "banana", "cherry"))
print(x)

x=bytes(5)
print(x)

x=bytearray(5)
print(x)

x=memoryview(bytes(5))
print(x)
