n=int(input("enter the number of values"))
a=[]
for i in range(5):
   c=int(input("enter the value"))
   if c>100:
      a.append("over")
   else:
    a.append(c)
print("list elements are:")
print(a)
