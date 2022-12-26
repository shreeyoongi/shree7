a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c=a
a=b
b=c
print('the value after swapping',a,b)

a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
print('the value before swapping',a,b)
a,b=b,a
print('the value after swapping',a,b)

a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
a=a+b
b=a-b
a=a-b
ptint('the value before swapping',a,b)
print('the value after swapping',a,b)

a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
print("the value before swapping",a,b)
a=a^b
b=a^b
a=a^b
print("the value after swapping",a,b)
