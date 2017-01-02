def f(x):
 if x==0:
     return[0]
 a=[0]*(x+1)
 a[1]=1
 for i in range(1,x):
     a[i+1]=a[i]+a[i-1]
 return a

print f(15)
