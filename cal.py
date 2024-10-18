def add(a,b): 
    return a + b

def sub(a,b):
    return a - b

def multi(a,b):
    return a * b

def div(a,b):
    return a / b

def cal():
    print("select choice:")
    print("1.add") 
    print("2.sub")
    print("3.multi")
    print("4.div")
    print("5.exit")
    while True:
            ch = int(input("Enter choice "))
            if ch == '5':
                print("Exit")
                break
            if ch in ['1', '2', '3', '4']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            if ch == '1':
                print("Result = {add(a,b)}")
            elif ch == '2':
                print("Result = {sub(a,b)}")
            elif ch == '3':
                print("Result = {multi(a,b)}")
            elif ch == '4':
                print("Result = {div(a,b)}")
    else:
        print("Invalid input")
    cal()    

            

