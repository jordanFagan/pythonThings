def f(r):
  x=""
  for i in range(r):
    x+=" "*(r-i)+"*"*(i+i+1)+"\n"
  return x

print f(12)
