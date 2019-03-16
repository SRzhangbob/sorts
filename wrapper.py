#!usr/bin/python
#coding:utf-8
import functools
import os

def logging(log_file='log.txt'):
    def _wrap(f):
        @functools.wraps(f)
        def _wrapper(*args, **kwargs):
            log_str = "{}, {}".format(f.__name__, "was called")
            file_dir = os.path.join(r"C:\Users\zhangbob\Desktop",log_file)
            with open(file_dir, 'w') as fb:
                fb.write(log_str)
            return f(*args, **kwargs)
        return _wrapper
    return _wrap


class logit(object):

    def __init__(self, file_dir="log.txt"):
        self._file_dir = file_dir

    def __call__(self, func):
        @functools.wraps(func)
        def _wrap(*args, **kwargs):
            log_str = "class {}, {}".format(func.__name__, "Called")
            file_dir = os.path.join(r"C:\Users\zhangbob\Desktop",self._file_dir)
            with open(file_dir, 'w') as fb:
                fb.write(log_str)
            return func(*args, **kwargs)
        return _wrap

@logit('1.txt')
@logging()
def Test():
    print("test")

@logit('g.txt')
@logging("log1.txt")
def Test2():
    print('test2')


if __name__ == '__main__':
    Test()
    Test2()