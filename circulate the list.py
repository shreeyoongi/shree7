v=int(input('enter the number of value in list'))
l=[]
for i in range (0,v):
    ele=int(input('enter the value'))
    l.append(ele)
print('circulating the list')
n=int(input('enter number of rotations'))
for i in range (0,n):
    l=l[1:]+l[:1]
    print('the circulated list after',i+1,'rotational',l)
