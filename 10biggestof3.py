a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))
'''
if a>b:
    if a>c:
        print(a,"is greator")
    else:
        print(b,"is greator")
else:
    if b>c:
        print(b,"is greator")
    else:
        print(c,"is greator")
'''
if (a>=b) and (b>=c):
  print(a,"is greater")
elif (b>=a ) and (b>=c) :
  print(b,"is greater")
else :
  print(c,"is greater")



