print("enter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
ls[0],ls[-1]=ls[-1],ls[0]
print(ls)