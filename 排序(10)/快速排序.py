# -*- coding: utf-8 -*-

# 选择一个基准元素（通常选择第一个元素）。
# 将序列分成两部分，所有比基准元素小的元素放在基准元素的左边，所有比基准元素大的元素放在基准元素的右边。
# 对左右两个子序列分别进行快速排序，直到序列为空或只有一个元素。
# 性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(logn)  3、非稳定排序  4、原地排序

def quick_sort(arr):
	sort(arr, 0, len(arr) - 1)

def sort(arr, low, high):
	if low < high:
		pivot_index = partition(arr, low, high)
		sort(arr, low, pivot_index - 1)
		sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1


arr = [4, 6, 5, 2, 3, 1, 7]
quick_sort(arr)
print(arr)

4, 6, 5, 2, 3, 1, 7

