class A(object):
    def name(self):
        print('name is jack')
        # super(A,self).name()


class B(object):
    def name(self):
        print('name is cat')


class C(A, B):
    def name(self):
        print('name is wang')
        super(C, self).name()


if __name__ == '__main__':
    c = C()
    c.name()
