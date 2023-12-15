class Time:
    def __init__(self,h,m,s):
        self.h1=h
        self.m1=m
        self.s1=s
    def __add__(self,x):
        sum1=self.h1+x.h1
        sum2=self.m1+x.m1
        sum3=self.s1+x.s1
        if(sum3>=60):
            sum3=sum3-60
            sum2=sum2+1
        if(sum2>=60):
            sum2=sum2-60
            sum1=sum1+1
        print(sum1,":",sum2,":",sum3)
print("Time1:")
h1=int(input("enter the hour :"))
m1=int(input("enter the minute :"))
s1=int(input("enter the second :"))
print("Time2:")
h2=int(input("enter the hour :"))
m2=int(input("enter the minute :"))
s2=int(input("enter the second :"))
obj1=Time(h1,m1,s1)
obj2=Time(h2,m2,s2)
print("sum of both are:")
obj1+obj2