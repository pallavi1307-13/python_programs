print("enter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
for item in ls:
    if item not in elements_to_remove:
        updated_list.append(item)
print("Updated list:", updated_list)


