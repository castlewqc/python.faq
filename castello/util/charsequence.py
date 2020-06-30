class CharSequence:
    @staticmethod
    def print(_input):
        print(_input, end='')

    @staticmethod
    def println(_input):
        print(_input)

    @staticmethod
    def print_iterate(inputs):
        it = iter(inputs)
        while True:
            try:
                print(next(it), end='')
            except StopIteration:
                break
        # print(inputs,sep='|',end='\r\n')
