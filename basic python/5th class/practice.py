'''
x = 2 #

print(type(x)) # wants to find the data type of x
y = float(x)
print(type(y)) #explicit casting
print(x)
print(y)

x = str(x)
print(type(x))

z = str(2) # implicit casting 
print(type(z))

x= str("s1")
y = str (2)
z = str(2.0)
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


a = "I love python, 2, i Like ML, 2.5"
print(a)
print(type(a))

a = [1,2,3,4,'sajib',2.0]
print(a)
print(type(a))


a = (1,2,3,4,'sajib',2.0)
print(a)
print(type(a))

a = {1,2,3,4,'sajib',2.5,2}
#a = [1,2,3,4,'sajib',2.0,2]
#a = (1,2,3,4,'sajib',2.0,2)
print(a)
print(type(a))



car ={
	"car_name": ['BMW','toyota','lamborgini'],
	"year" : [2020,2021,2022]
}
print(car)

import pandas as pd
df = pd.DataFrame(car)
print(df)

# String Operation


a = "hello"
b = "python"

new_val = a +' '+ b
#print(new_val)
#print(f'the {new_val} ::-- is the concatenation of these two varibales')

print('The {} ::-- is the concatenation of these two variables'.format(new_val))



#str1 ="i love python" (practice)



#slicing
new = "i love python"
new_val = new[0:6]
new_va = new[-2]
print(new_va)


new = "i love python"
#new_v = new[4 :]
new_v = new[-1 : -6: -2]
new_v = new[1 : 6: 2]
print(new_v)




# MEMBER 
new = "i love python"
print("love" in new)
print("Machine" in new)



# methods

new = "i love python"
print(new.lower())
print(new.upper())
print(new.replace("love","like"))


a = "textbook"
b = "mictest"
print(a.removeprefix("text"))
print(b.removesuffix("test"))
'''















