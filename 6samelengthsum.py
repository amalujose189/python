l1=[1,2,45,78,98]
l2=[3,6,87,9,12,5]
print("list: ",l1)
print("list2: ",l2)
print("length of list1=",len(l1))
print("length of list2=",len(l2))
if len(l1)==len(l2):
    print("length are same")
else:
    print("length are not same")
print("sum of list1=",sum(l1))
print("sum of list2=",sum(l2))
if sum(l1)==sum(l2):
    print("sum of two lists are same")
else:
    print("sum of list are not same")
check=any(item in l1 for item in l2)
print("any value occur in both:",check)