# -*- coding: utf-8 -*-

# 循环次数为数组的长度
# 每次循环的项的数量 - 1
# 依次比较相邻两项的值，并将较小项放置在较大项之前
# 优化版。如果相邻两个数均为发生交换，则表示数组已为有序数组
# 性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

def bubble_sort(arr):
	if (not isinstance(arr, list)) or len(arr) < 2:
		pass
	
	for i in range(len(arr)):
		changed = False
		for j in range(len(arr) - i - 1):
			if arr[j + 1] < arr[j]:
				arr[j], arr[j+1], changed = arr[j + 1], arr[j], True
		if not changed: #优化版，如果相邻两个数均为发生交换，则表示数组已为有序数组
			break 

arr = [2, 1, 5, 4, 3]
bubble_sort(arr)
print(arr)
