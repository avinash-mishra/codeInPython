class ClassA(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = 2

    def methodA(self):
        self.var3 = self.var1 + self.var2
        return self.var3

class ClassB(ClassA):
    def __init__(self, class_a):
        self.var1 = class_a.var1
        self.var2 = class_a.var2

object1 = ClassA()
sum = object1.methodA()
print(sum)