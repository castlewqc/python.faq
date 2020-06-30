import time
import datetime

if __name__ == '__main__':
    print(time.gmtime())  # GMT时间
    print(time.localtime())
    print(time.localtime(1))
    print(time.mktime(time.localtime(1)))  # 秒数
    print(time.asctime())  # Tue Jun 23 22:34:48 2020
    print("ctime:" + time.ctime())  # -> asctime(localtime(secs))
    time_format = "%Y-%m-%d %H:%M:%S"
    time_str = time.strftime(time_format)
    print(time_str)
    print(time.strptime(time_str, time_format))  # 根据格式解析表示时间的字符串 返回struct_time
    # 月份值是 [1,12] 的范围，而不是 [0,11]  tm_wday range [0, 6] ，周一为 0 tm_yday range [1, 366]
    print(time.time())  # 时间戳

    now_day = datetime.date.today()
    print(now_day)  # 2020-06-23
    next_day = datetime.date(2020, 6, 25)
    print(now_day.__sub__(next_day))
    print(now_day.__rsub__(next_day))
    print(datetime.date.fromtimestamp(time.time()))

    print("datetime.datetime.now():{0}".format(datetime.datetime.now()))  # 2020-06-23 23:16:47.629175
    print(datetime.datetime.now().time())  # 23:16:47.629175

    # https://docs.python.org/zh-cn/3/library/datetime.html#module-datetime
    print(datetime.datetime.now() + datetime.timedelta(hours=10))
