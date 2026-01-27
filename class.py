class A:
    def f1(self):
        return "Method f1 from class A"
    def f2(self):
        return "Method f2 from class A"
class B(A):
    def f3(self):
        return "Method f3 from class B"
        A.f1(self)
    def f4(self):
        return "Method f4 from class B"
a=A()
b=B()   
print(b.f3())
#super is used to call parent class methods is notdefinitely needed here
#super function check the value of next in mro and calls that method
print(super(B,b).f1())
#mro is method resolution order which is the order in which python looks for a method in a hierarchy of classes
print(b.f1())
class A:
    def f1(self):
        return "Method f1 from class A"
    def f2(self):
        return "Method f2 from class A"
class B(A):
    def f3(self):
        return "Method f3 from class B"
        A.f1(self)
    def f4(self):
        return "Method f4 from class B"
class c(A):
    pass
class D(c,B):
    pass
    super().f1()
    super().f3()    
    super().f2()

#diamond problem diamond problem occurs when two classes B and C inherit from A and class D inherits from both B and C
#in this case if we call a method from class A using an object of class D python uses mro to determine which method to call
a=A()
b=B()
C=c()
d=D()
print(D.__mro__)