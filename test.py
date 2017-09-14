class MyClass:
    static_elem = 123
    

    def __init__(t):
        t.object_elem = 456
    @staticmethod
    def add(t):
        t.add2=1;

c1 = MyClass()
c2 = MyClass()
c1.add()
print(c1.add2)
