class company:
    def fun1(self):
        print("comp fun")
class colour(company):
    def fun2(self):
        print("sub 1")
class product(company):
    def fun3(self):
        print("sub 2")
obj = product()
obj.fun3()
obj.fun1()
obj2 = colour()
obj2.fun2()
