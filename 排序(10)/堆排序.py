# -*- coding: utf-8 -*-

"""
堆排序(Heap Sort)是一种基于二叉堆的排序算法。它利用了二叉堆的性质来进行排序, 具有稳定的时间复杂度和较好的空间效率。

堆排序的基本思想是将待排序的元素构建成一个二叉堆，然后逐步将堆顶元素（最大值或最小值）取出，放到已排序部分的末尾，再重新调整剩余元素构成的堆，重复这个过程直到所有元素都被取出并放置到正确的位置上。

以下是堆排序的一般步骤：

构建最大堆（或最小堆）：将待排序的元素构建成一个最大堆（或最小堆）。最大堆的性质是父节点的值大于或等于其子节点的值，最小堆的性质是父节点的值小于或等于其子节点的值。

取出堆顶元素：将堆顶元素（最大值或最小值）取出，并放置到已排序部分的末尾。

调整堆：将剩余元素重新调整为一个最大堆（或最小堆）。

重复步骤2和步骤3, 直到所有元素都被取出并放置到正确的位置上。

堆排序的时间复杂度是O(n log n), 其中n是待排序数组的长度。它具有较好的空间效率, 因为它是就地排序, 不需要额外的空间。

"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    print('heapify', arr)

def heap_sort(arr):
    n = len(arr)
    
    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        print(i)
        heapify(arr, n, i)
    print('max', arr)

    # 取出堆顶元素，重建堆
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(arr)
        heapify(arr, i, 0)


arr = [4, 6, 5, 7, 3, 1, 2]
heap_sort(arr)
print(arr)