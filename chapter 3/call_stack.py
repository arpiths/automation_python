# the call stack
#  a 
#  a -> b
#  a -> b ->c
#  a -> b
#  a 
#  a -> d
#  a 

def a():
    print("a start")
    b()
    d()
    print("a return")

def b():
    print("b start")
    c()
    print("b return")

def c():
    print("c start")
    print("c return")

def d():
    print("d start")
    print("d return")

a()