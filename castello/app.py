from castello.pojo import Student
import os
from castello.util.charsequence import CharSequence

if __name__ == '__main__':
    jack = Student('jack')
    print(jack.__len__())
    print(jack.__dict__)
    print(jack.len())
    print(type(jack))
    print(dir(jack))
    print(jack.age)
    jack.cry()
    jack.farther = "Jack's farther"
    print(jack.farther)
    print(hasattr(jack, 'age'))

    print(os.listdir('.'))
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    print('a', 'b', sep='|', end='')
    CharSequence.print('c')
    CharSequence.println('d')
    CharSequence.println('e')
    CharSequence.printIterate([x for x in range(1, 11) if x > 5])
