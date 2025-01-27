'''
print("Data science ","\n","Data science")

print("Data science ","Data science", sep ="\n")


#Addition 
print(3+2)
#substraction
print(4-2)
# multiplication
print(3*5)
#power
print(3**3)
#div
print(25/5)
print(25/6)

print(25//6)
print(23//5)
print(-5//2)
print(5//2)

#mod
print(10%3)

# variable
print("a")

a = ("i am python")
print(a)

myName= "sajib"
print(myName)
MyName =  "sajib"
print(MyName )


_name = "hello python"
print(_name)
@name = "hello python"
print(-name)

variable types: local and global 

A function is a block of code designed to perform a specific task. 
It takes input (called parameters), processes it, 
and often returns a result. Functions help organize code, 
making it reusable and easier to understand.

# local variable
def add():
	a = 2
	b = 3
	c = a + b
	return c

print(add())

# global variable
a = 3
b = 5
def add():
	
	c = a + b
	return c

print(add())

a = 3
b = 5
def add():
	a = 2
	b = 5
	c = a + b
	return c

print(add())
# data type check
b= "name"
print(type(b))


b= "cr7"
print(type(b))

c = 2
print(type(c))


d = True
print(type(d))

f = 2.5
print(type(f))

# user input 
a = input() # by default it takes input as string 
print(a)
print(type(a))

a = int(input())
print(a)
print(type(a))


a = float(input())
print(a)
print(type(a))


a = int(input())
print(a)
print(type(a))

# addition by taking user input

a = int(input())
b = int(input())
print(a+b)

a = int(input("enter the 1st number:---"))
b = int(input("enter the 2nd number :---"))
print(a+b)


greet = "hello"
name = "sajib"
print("\n",greet  +' '+ name)



a = str(input("enter any name"))
b = str(input("enter 2nd name"))
print(a + b)


# key word will not be a variable 
for = 10
print(for)


if = 20
print(if)

import keyword
print(keyword.kwlist)

X , Y ,Z = "i", "LOVE", "PYTHON"
print(X)
print(Y)
print(Z)
'''
X , Y ,Z = "i", "LOVE", "PYTHON"
a = Y.find("O")
print(a)
b = Y.find("E")
print(b)











