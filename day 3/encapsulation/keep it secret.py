class myClass:
    __privateVar = 27;
def privMeth(self):
    print("I am inside class myclass")
def hello(self):
    print("private variable value:", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth()
