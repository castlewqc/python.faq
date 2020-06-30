# 单前导下划线：_var 约定，提示 以单个下划线开头的变量或方法仅供内部使用 可以访问，但不会导入
# 单末尾下划线：var_ 约定，解决与关键字重名
# 双前导下划线：__var 触发名称修饰（name mangling） - 解释器更改变量的名称，以便在类被扩展的时候不容易产生冲突。
# 双前导和末尾下划线：__var__ 避免触发名称修饰 不建议使用
# 单下划线：_ 除了用作临时变量之外，“_”是大多数Python REPL中的一个特殊变量，它表示由解释器评估的最近一个表达式的结果。


# 1. 变量命名总结：
# - 1.单下划线开头变量：protected
# - 2.双下划线开头变量：private
# - 3.双下划线开头，双下划线结尾：系统内置变量
# 2. 函数命名总结：
# - 1.私有方法：小写和一个前导下划线
# - 2.特殊方法（魔术方法）：小写和两个前导下划线，两个后置下划线
# - 3.函数参数：小写和下划线，缺省值等号两边无空格
# 3. 类名称命名：
# - 类总是使用驼峰格式命名，即所有单词首字母大写其余字母小写。

class UnderlineParent:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 37  # __baz -> _UnderlineParent__baz


class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled


if __name__ == "__main__":
    p = UnderlineParent()
    print(dir(p))
    print(p._UnderlineParent__baz)

    print(ManglingTest().get_mangled())  # hello
