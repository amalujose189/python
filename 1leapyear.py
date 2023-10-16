current_y=int(input("enter the current year:"))
final_y=int(input("enter the final year:"))
print("leap years are:")
for i in range(current_y,final_y):
    if(i%4==0) and (i%100!=0) or (i%400==0):
        print(i)