s=int(input('enter the value in list:'))
list=[]
for i  in range (0,s) :
    element=int(input("enter the value"))
    list.append(element)
print('circulating the list')
for i in range (0,s) :
     element_deleted=list.pop(0)
     list.append(element_deleted)
     print('the circulatedlist after',i+1,'rotation',list)
