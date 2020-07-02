import  decimal
if __name__ == '__main__':
    print(round(2.675, 2))  # 2.67 这是个坑，除非对精度没有要求，不然不要用round
    print('%.2f' % 2.676)
