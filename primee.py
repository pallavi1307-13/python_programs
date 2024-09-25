print("ennter the elements in the list")
n=int(input())
ls=[]
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
for j in ls:
    for i in range(2,j):
            if(j%i==0):
                print("not prime")
                break
    else:
        print("prime")

