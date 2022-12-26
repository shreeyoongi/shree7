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
print('the value after swapping',a,b)


x1=int(input('enter the value of a'))
x2=int(input('enter the value of b'))
y1=int(input('enter the value of y1'))
y2=int(input('enter the value of y2'))
d=(x1-x2)+(y1-y2)**2
r=d**0.5
print('the distance is',r)


s=int(input('enter tne value in list :'))
list=[]
for i in range(0,s):
    element=int(input('enter the value:'))
    list.append(element)
print('circulating the list')
for i in range (0,s):
     element_deleted=list.pop(0)
     list.append(element_deleted)
     print('the circulated list after',i+1,'rotation',list)
    
