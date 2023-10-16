a=str(input("enter the first string\n"))
b=str(input("enter the second string\n"))
print(a.replace(a[0],b[0])+' '+b.replace(b[0],a[0]))