print("enter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
n2=int(input("the check element"))
is_present=False
for i in range(len(n)):
    if n[i]==n2:
        is_present = True
        break
if is_present:
    print("is present")
else:
    print("not present")
