def circulate (c,n):
    for i in range (1,n+1):
     d=c[i:]+[:i]
print('circulate','=',d)
    return
c=(123,234,345,456,567,678,789,312,143,364)
n=iint(input('enter n :'))
circulate(c,n)
