#a = c b = d c = a d = b
a = input("Enter first variable :")
b = input("Enter second variable :")
c = input("Enter third variable :")
d = input("Enter fourth variable :")
e = a
a = c
c = e
f = b 
b = d
d = f
print(a)
print(b)
print(c)
print(d)