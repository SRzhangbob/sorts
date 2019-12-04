#!user/bin/python
# 写的排序算法
# 本文件基于python3
import random
import unittest


# 归并算法的合并
# 看起来非常丑陋
def Merge(numlist, start, mid, end):
    i = start
    j = mid + 1
    t = []
    k = 0
    while(i <= mid and j <= end):
        if(numlist[i] <= numlist[j]):
            t.append(numlist[i])
            k += 1
            i += 1
        else:
            t.append(numlist[j])
            k += 1
            j += 1
    while(i <= mid):
        t.append(numlist[i])
        k += 1
        i += 1
    while(j <= end):
        t.append(numlist[j])
        k +=1
        j += 1
    for i in range(0, k):
        numlist[start + i] = t[i]

# 递归的归并算法
def Merge_Sort(numlist, start, end):
    if not numlist or start >= end:
        return
    mid = (start+end)//2
    Merge_Sort(numlist, start, mid)
    Merge_Sort(numlist, mid+1, end)
    Merge(numlist, start, mid, end)

# 就地快排
def QuickSortJust(numList, start, end):
    if start >= end:
        return
    low = start
    high = end
    pivot = numList[end]
    while(low < high):
        while(low < high and numList[low] <= pivot):
            low += 1
        numList[high] = numList[low]
        while(low < high and numList[high] > pivot):
            high -= 1
        numList[low] = numList[high]
    numList[low] = pivot
    QuickSortJust(numList, start, low-1)
    QuickSortJust(numList, low+1, end)

# 随机选择pivot的非就地快排
def RandomQuicksort(numList):
    import random
    iLength = len(numList)
    if iLength <= 1:
        return numList
    index = random.randint(0, len(numList)-1)
    pivot = numList[index]
    return RandomQuicksort([numList[i] for i in range(len(numList))if numList[i] <= pivot and i!=index])\
           + [pivot] + RandomQuicksort([i for i in numList if i > pivot])

# 非随机选择pivot的非就地快排
def Quicksort(numList):
    iLength = len(numList)
    if iLength <= 1:
        return numList
    pivot = numList[0]
    return Quicksort([i for i in numList[1:] if i <= pivot]) + [pivot] + Quicksort([i for i in numList[1:] if i > pivot])

# 比较列表是否相等
def CmpListEqual(numlist, othernumlist):
    if len(numlist) != len(othernumlist):
        return False
    for num, anothernum in zip(numlist, othernumlist):
        if num != anothernum:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


# 测试用例
def UnitTest():
    for i in range(50):
        Numlist = [random.randint(0, 1000) for i in range(100)]
        Numlist2 = Numlist[:]
        Numlist.sort()
        sortNumList = Quicksort(Numlist2)
        Merge_Sort(Numlist2, 0, len(Numlist2)-1)
        print("UnitTest", CmpListEqual(Numlist, sortNumList))
        print("UnitTest1", CmpListEqual(Numlist, Numlist2))

class TestSortMethod(unittest.TestCase):
    """
    TestSortMethod
    """
    @classmethod
    def setUpClass(cls):
        print("run once start")

    @classmethod
    def tearDownClass(cls):
        print("run once end")

    def setUp(self):
       self.Numlist = [random.randint(0, 1000) for i in range(100)]
       self.Numlist_2 = self.Numlist[:]
       self.Numlist_2.sort()
       print("test start")

    @unittest.skip("don't want to test it")
    def test_QuickSort(self):
        self.assertEqual(Quicksort(self.Numlist), self.Numlist_2)

    def test_RandomQuicksort(self):
        self.assertEqual(RandomQuicksort(self.Numlist), self.Numlist_2)

    def test_Test(self):
        self.assertEqual(Test()(), "fasfda")

    def tearDown(self):
        print("test end")

def suite():
    suite = unittest.TestSuite()
    suite.addTests([TestSortMethod('test_QuickSort'), TestSortMethod('test_RandomQuickSort'),
                    TestSortMethod('test_Test')])
    return suite

class Test(object):

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return "fasfda"

if __name__ == "__main__":
    UnitTest()
    # unittest.main()

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
