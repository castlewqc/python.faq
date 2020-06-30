class A(object):
    a = 'a'

    @staticmethod
    def foo1(name):
        print('hello', name)
        print(A.a)  # 正常
        print(A.foo2(
            'name'))  # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)

    def foo2(self, name):
        print('hello', name)

    @classmethod
    def foo3(cls, name):
        print('hello', name)
        print(A.a)  # 正常
        print(cls().foo2(name))
# https://blog.csdn.net/sinat_33718563/article/details/81298785
# 既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
# 从它们的使用上来看,
# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
# @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
# 如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
# 而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。