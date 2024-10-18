print("enter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
largest = ls[0]
for num in ls:
    if num > largest:
        largest = num
print("Largest:", largest)
