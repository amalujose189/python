n=str(input("enter the string"))
if n[len(n)-3:]!="ing":
    print(n+"ing")
else:
    print(n+"ly")
