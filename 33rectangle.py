class rect:
    def __init__(self,l,b):
        self.a1=l
        self.a2=b
    def area(self):
        self.m=self.a1*self.a2
    def peri(self):
        self.p=2*(self.a1+self.a2)
    def dipslay(self):
        print("area of a rectangle =",self.m)
        print("perimeter of a rectangle=",self.p)
    def compare(self,obj2):
        if(self.m==obj2.m):
             print("area are same")
        elif(self.m>obj2.m):
             print("area of the first rectangle is greator")
        else:
            print("area of the second is greator")
l1=int(input("enter the length of first rectangle"))
b1=int(input("enter the breadth of first rectangle"))
l2=int(input("enter the length of second rectangle"))
b2=int(input("enter the breadth of second rectangle"))
obj1=rect(l1,b1)
obj2=rect(l2,b2)
obj1.area()
obj1.peri()
obj2.area()
obj2.peri()
obj1.dipslay()
obj2.dipslay()
obj1.compare(obj2)
