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


# 根据路径返回一个类
# 详情请查看文章《实现参数决定函数内部创建其他模块的类》
def import_module(dotted_path):
    """
    Imports the specified module based on the
    dot notated import path for the module.
    """
    import importlib

    module_parts = dotted_path.split('.')
    module_path = '.'.join(module_parts[:-1])
    module = importlib.import_module(module_path)

    return getattr(module, module_parts[-1])



def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    """
    打印进度条
    Print progress bar
    :param description: Training description
    :type description: str

    :param iteration_counter: Incremental counter
    :type iteration_counter: int

    :param total_items: total number items
    :type total_items: int

    :param progress_bar_length: Progress bar length
    :type progress_bar_length: int

    :returns: void
    :rtype: void
    """
    import sys

    percent = float(iteration_counter) / total_items
    hashes = '#' * int(round(percent * progress_bar_length))
    spaces = ' ' * (progress_bar_length - len(hashes))
    sys.stdout.write("\r{0}: [{1}] {2}%".format(description, hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    if total_items == iteration_counter:
        print("\r")

