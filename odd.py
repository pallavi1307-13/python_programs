print("enter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
for num in ls:
    if num % 2 !=0:
        print(num)