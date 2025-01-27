'''
x = "I love Machine Learning"
print("The output from varibale x is :--", x)

x = "I love Machine Learning"
print(x.upper())

x = "i love Machine Learning"
y = x.upper()
print(y)
print(x)


y = x.capitalize()
z = x.upper()
s = x.lower()
print("original x is : -",x)
print("capitalize form of x is :--",y)
print("Uppercase form of x is : ---",z)
print("lower form of x is : ---",s)


x = "i love machine learning"
y = x.replace("love", "like")
print(y)

k = 10
def value():
	x = 20
	print(x + k )
print(value())


k = 10
def value():
	x = 20
	k = 5
	y = k + x
	z = k - x
	return z,y
print(value())



x = 30
y = 20

if x > y:
	print("Ture")
else:
	print("false")


any = 20

if any==20:
	print("can purchase the product")
else:
	print("not able to purchese")



any = 20

if any <= 20:
	print("can not  purchase the product")
else:
	print("able to purchese")



a = 20
b = 20

if a > b:

	print("a is greater than b")


elif a == b:

	print(" a and b are equal")
else:

	print(" a is  less than b ")




any = 20
product = 15

if any > product:
	print("buy")
elif any == product:
	print("buy and your balance is now empty")
else:
	print("not able to buy")


a = 20
b = 2
c = 10

if a > b:
	
	if b > c:
		print("buy")
	else:
		print("not")
else:
	print("not valid")

	
x = 10
y = 10
if x > y:
	print("Ture")
elif y > x:
	if y%2 == 0:
		print("it even")
	else:
		print("odd")


else:
	print("false")

a = input()
print(a)
print(type(a))

'''

a = int(input("please give a intger number:--"))

if a > 90:
	print('a is greater than 90')

	if a > 95 and a <100:
		print("a is in between 95 to 100")
	else:
		print("a is less than 95 or greater than 100")

elif a ==90:
	print("a is equal to 90")
else:
	print("a is less than 90")
















