print("Area of rectangle")
len=int(input("enter the length"))
bread=int(input("enter the breadth"))
c=lambda x,y:x*y
print("Area of rectangle :"+str(c(len,bread)))
print("Area of square ")
s=int(input("enter the side"))
c=lambda x:x*x
print("Area of square="+str(c(s)))
print("Area of triagle")
l=int(input("enter the length"))
b=int(input("enter the breadth"))
c=lambda x,y:0.5*l*b
print("Area of triangle :"+str(c(l,b)))

