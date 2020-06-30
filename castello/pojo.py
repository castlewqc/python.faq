class Human(object):
    def __init__(self):
        self.age = 0

    def cry(self):
        print('cry')

    @staticmethod
    def static_method():
        print('static method')

    @classmethod
    def clz_method(clz):
        print('class method')


# 不继承属性 只继承方法
class Student(Human):
    gender = 0
    __slots__ = ('farther','mother')

    def __init__(self, name):
        self.__name = name
        self.age = 0;

    def __len__(self):
        return len(self.__name)

    def len(self):
        return self.__len__()
