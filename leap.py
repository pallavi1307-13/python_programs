print("enter year")
n=int(input("enter a year"))
if(n%400==0 or n%4==0 and n%100!=0):
    print("leap year")
else:
    print("not leap year")