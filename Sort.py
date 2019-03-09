#!user/bin/python
# 写的排序算法
# 本文件基于python3


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
def Quicksort2(numList):
    iLength = len(numList)
    if iLength <= 1:
        return numList
    pivot = numList[0]
    return Quicksort2([i for i in numList[1:] if i <= pivot]) + [pivot] + Quicksort2([i for i in numList[1:] if i > pivot])

# 比较列表是否相等
def CmpListEqual(numlist, othernumlist):
    if len(numlist) != len(othernumlist):
        return False
    for num, anothernum in zip(numlist, othernumlist):
        if num != anothernum:
            return False
    return True

# 测试
def UnitTest():
    import random
    for i in range(50):
        Numlist = [random.randint(0, 1000) for i in range(100)]
        Numlist2 = Numlist[:]
        Numlist.sort()
        sortNumList = Quicksort2(Numlist2)
        Merge_Sort(Numlist2, 0, len(Numlist2)-1)
        print("UnitTest", CmpListEqual(Numlist, sortNumList))
        print("UnitTest1", CmpListEqual(Numlist, Numlist2))


if "__name__" == "__main__":
    UnitTest()
