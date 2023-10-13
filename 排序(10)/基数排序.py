# -*- coding: utf-8 -*-

"""
基数排序(Radix Sort)是一种非比较排序算法, 它根据元素的位数进行排序。基数排序的基本思想是将待排序的元素按照低位到高位的顺序依次进行排序, 直到最高位排序完成，从而得到有序序列。

基数排序的主要步骤如下：

确定待排序元素的最大值，并计算出最大值的位数。这将决定需要进行多少轮排序。

创建10个桶, 每个桶对应0到9的数字。

从最低位开始，将待排序元素按照当前位数上的数字分配到对应的桶中。

按照桶的顺序将元素取出，并将它们合并到一个新的数组中。

重复步骤3和步骤4, 直到最高位排序完成。

返回排序完成后的数组。

基数排序的关键在于将元素按照位数进行分配和收集。在每一轮排序中，元素被分配到桶中后，按照桶的顺序将元素取出，再进行下一轮排序。通过多轮的分配和收集，最终可以得到有序的结果。

基数排序适用于待排序元素的位数较小且范围较小的情况。它的时间复杂度是O(d * (n + k)), 其中d是最高位数, n是待排序数组的长度, k是桶的数量。基数排序的空间复杂度是O(n + k), 其中n是待排序数组的长度, k是桶的数量。
"""

def radix_sort(arr):
	max_num = 0
	for val in arr:
		if max_num < val:
			max_num = val

	max_digits = len(str(max_num))

	for digit in range(max_digits):
		buckets = [[] for _ in range(10)]
		for num in arr:
			radix_num = radix(num, digit)
			buckets[radix_num].append(num)

		arr = []
		for bucket in buckets:
			arr.extend(bucket)
	return arr
		

def radix(num, digit):
	return num // (10 ** digit) % 10
	

arr = [1, 4, 3, 5, 2, 32, 45, 47, 100, 120, 130, 1000]
arr = radix_sort(arr)
print(arr)