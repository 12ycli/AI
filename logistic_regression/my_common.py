# 时间测量的装饰器
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f s' % (f.__name__, (time2-time1)*1000000.0))
        return ret
    return wrap


def print_result_after(f):
    def wrap(*args):
        ret = f(*args)
        print(ret)
        return ret
    return wrap



