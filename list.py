#append()
fruits = ["apple", "banana", "cherry"]
f=[]
for i in fruits:
    f.append(i)
for i in f:
    print(i)
#fruits.append("orange")

print(fruits)
#clear()
name = ["ammu","arju"]
for i in name:
  print(i)
name.clear()
print(name)
#copy
fruits = ["apple", "banana", "cherry"]
f = []
x = fruits.copy()
print(x)

for i in fruits:
    f = fruits.copy()
    print(i)
print(f)
