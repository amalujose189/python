class Rectangle:
    def __init__(self,l,b):
         self.l1=l
         self.b1=b
    def area(self):
        area1=self.l1*self.b1
        return area1
    def __lt__(self, obj):
        if (self.area()<obj.area()):
            print("area of rectangle 1 is less than area of rectangle 2")
        else:
            print("area of rectangle 2 is less than area of rectangle 1")
print("RECTANGLE 1")
l1=int(input("enter the length of 1st rectangle"))

b1=int(input("enter the breadth of 1st rectangle"))
print("RECTANGLE 2")
l2=int(input("enter the length of 2nd rectangle"))
b2=int(input("enter the breadth of 2nd rectangle"))
obj1=Rectangle(l1,b1)
obj2=Rectangle(l2,b2)
print("area first rectangle")
print(obj1.area())
print("area second rectangle")
print(obj2.area())
print("Now Comparing The Rectangles")
print(obj1 < obj2)