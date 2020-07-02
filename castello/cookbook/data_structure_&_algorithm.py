def sequence_2_variable():
    print('sequence2variable')
    p = (4, 5)
    x, y = p
    print('x={0},y={1}'.format(x, y))
    s = 'hello'
    _, e, l, _, _ = s  # _选一个用不到的变量名，以此作为要丢弃的值的名称
    print('e={0},l={1}'.format(e, l))
    print('sequence2variable')


def drop_first_last(args):
    first, *middle, last = args
    return middle


def drop_first_last_parameters(*args):
    first, *middle, last = args
    return middle


from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    sequence_2_variable()
    print(drop_first_last((1, 2, 3, 4)))
    print(drop_first_last_parameters(1, 2, 3, 4, 5))
    score = (89, 73, 31, 69, 'jack')
    *mark, name = score
    print('%.3f' % (sum(mark) / len(mark)))  # python 除法 /，//（整除，向下取整）

    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print('-' * 20)
