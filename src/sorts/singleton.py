import functools
import time
import threading

#1、把整个模块作为一个单例
#2、使用装饰器
def Singleton(cls):
    _instance = {}
    @functools.wraps(Singleton)
    def _wrap(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _wrap


def RunTime(func):
    @functools.wraps(RunTime)
    def _warp(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("[{}]cost:{}".format(func.__name__, end-start))
    return _warp


class Test(object):
    _instance_lock =  threading.Lock()

    def __init__(self):
        time.sleep(1)

# 3、使用类函数实现
    @classmethod
    def instance(cls, *args, **kwargs):
        with Test._instance_lock:
            if not hasattr(Test, "_instance"):
                    Test._instance = Test(*args, **kwargs)
        return Test._instance


# 4、使用类函数，线程安全，可以优化，先判断是否有类实例，再枷锁，减少开销
    @classmethod
    def instance1(cls, *args, **kwargs):
        if not hasattr(Test, "_instance"):
            with Test._instance_lock:
                if not hasattr(Test, "_instance"):
                        Test._instance = Test(*args, **kwargs)
        return Test._instance

 # 5、（推荐）使用new函数，加锁，可以实现线程安全的单例模式，推荐，而且可以不改变实例的初始化方式
    def __new__(cls, *args, **kwargs):
        if not hasattr(Test, "_instance"):
            with Test._instance_lock:
                if not  hasattr(Test, "_instance"):
                    Test._instance = object.__new__(cls)
        return Test._instance


def task(arg):
    obj = Test.instance()
    print(arg, obj, )

def newtask(arg):
    obj = Test.instance1()
    print(arg, obj)

def newnewtask(arg):
    obj = Test()
    print(arg, obj)

def UnitTest():
    oTestlst = []
    for i in range(0, 10):
        oTestlst.append(Test())
    for oTest in oTestlst:
        print(oTest)

def UnitThreadTest():
    for  i in range(0, 10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

def UnitThreadLockTest():
    for  i in range(0, 10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

@RunTime
def UnitThreadLockTestUpdate():
    for  i in range(0, 10):
        t = threading.Thread(target=newtask, args=[i, ])
        t.start()

@RunTime
def UnitThreadLockTestNew():
    for  i in range(0, 10):
        t = threading.Thread(target=newnewtask, args=[i, ])
        t.start()

if __name__ == "__main__":
    # 1‘测试UnitThreadTest()
    """这个是多线程情况下的单例测试，在非io情况下，Cpython的GIL没有释放的情况下，执行时正常的
        但是加入io（cpython会优化这种情况下的性能表现，释放GIL锁给其他线程执行），造成单例模式
        不再全局唯一，这种情况下需要加锁来保证
    0 <__main__.Test object at 0x000001C95531B3C8>
452  3<__main__.Test object at 0x000001C95548AA90><__main__.Test object at 0x000001C95548A7F0> 

<__main__.Test object at 0x000001C95548A8D0>
1 <__main__.Test object at 0x000001C95548A710> <__main__.Test object at 0x000001C95548A9B0>

9 768<__main__.Test object at 0x000001C95548AE10> <__main__.Test object at 0x000001C95548AC50>

 <__main__.Test object at 0x000001C95548AD30>
 <__main__.Test object at 0x000001C95548AB70>
    """
    # 2、UnitThreadLockTest()
    """
    这个是多线程加锁情况下的单例测试，在有io情况下，Cpython的GIL释放给其他线程执行，但加锁之后
    单例模式全局唯一，
    01  2<__main__.Test object at 0x000001E8C038B3C8>
 <__main__.Test object at 0x000001E8C038B3C8>
<__main__.Test object at 0x000001E8C038B3C8>345
  <__main__.Test object at 0x000001E8C038B3C8>
 <__main__.Test object at 0x000001E8C038B3C8>
6<__main__.Test object at 0x000001E8C038B3C8>7 8
<__main__.Test object at 0x000001E8C038B3C8>9 <__main__.Test object at 0x000001E8C038B3C8>
 <__main__.Test object at 0x000001E8C038B3C8>

 <__main__.Test object at 0x000001E8C038B3C8>
    """
    # 3、UnitThreadLockTestUpdate()，测试结果与2类似
   #4、 UnitThreadLockTestNew()
    """依赖于线程加锁和new方法执行在init方法之前可以实现
    实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
    实例化对象；然后再执行类的__init__方法，
    [UnitThreadLockTestNew]cost:0.0034349099999999994
0 <__main__.Test object at 0x00000278544EA978>
12 3<__main__.Test object at 0x00000278544EA978> 
<__main__.Test object at 0x00000278544EA978>
 <__main__.Test object at 0x00000278544EA978>
65 <__main__.Test object at 0x00000278544EA978>
4  <__main__.Test object at 0x00000278544EA978><__main__.Test object at 0x00000278544EA978>

89 7 <__main__.Test object at 0x00000278544EA978> <__main__.Test object at 0x00000278544EA978>

<__main__.Test object at 0x00000278544EA978>
    """