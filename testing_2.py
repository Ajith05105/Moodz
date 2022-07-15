class MyClass:
    var1 = 1

    @classmethod
    def update(cls, value):
        cls.var1 += value

    def __init__(self,value):
        self.value = value
        self.update(value)

a = MyClass(7)
print (MyClass.var1)
