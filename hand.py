print("1. create account")
print("2. withdraw ")
print("3. deposit")
print()

op = int(input())
if op == 1:
    name = str(input("enter your name"))
    age = int(input("enter your age ")) 

    if age < 18:
        raise ValueError("negative values are nt allowed")
        
    class raise ValueError(Exception):
        pass
    try:
        age = int(age)
    except ValueError as e:
        print(e)    
elif op == 2:
    amount = float(input("enter the amount"))
    if amount < 500:
        raise (Exception):


print("1. create account")
print("2. withdraw ")
print("3. deposit")
print()

op = int(input())





    
