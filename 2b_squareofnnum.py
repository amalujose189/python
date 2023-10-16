n=int(input("enter the limit"))
lst=[]
print("enter the elements")
for i in range(0,n):
    a=int(input())
    lst.append(a)
print("list is :",lst)
print("square of n numbers are:")
for i in lst:
    print(i,"=",i*i)
