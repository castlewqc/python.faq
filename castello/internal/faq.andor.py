# and or 从左往右执行
# python中0,'',[],{},(),None为false，其他都为true
# python中and or 返回的不是真假，而是实际比较的值之一
# or 执行到第一个为真就返回,不然返回最后一个值
# and 执行到第一个为假就返回，不然返回最后一个值

print(0 or "a" or 1)
print("a" and "b" and "c")
print("a" and "b" and 0 and "c")