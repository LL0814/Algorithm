# -*- coding: utf-8 -*-

# 递归使用二分法把源数组分成两个子数组，直到其中一个子数组的长度为 1。 
# 循环比较两个子数组的第一个项，并将较小值依次添加到返回数组中，同时移除该值。
# 最后将剩余项一次性添加到返回数组中。
# 性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(n)  3、稳定排序  4、非原地排序

def merge_sort(arr):
	if (not isinstance(arr, list)) or len(arr) < 2:
		return arr
	
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	
	left = merge_sort(left)
	right = merge_sort(right)
	return merge(left, right)

def merge(left, right):
	arr = []
	while len(left) > 0 and len(right) > 0:
		if left[0] > right[0]:
			arr.append(right[0])
			right.pop(0)
		else:
			arr.append(left[0])
			left.pop(0)

	if len(left) == 0:
		arr.extend(right)
	elif len(right) == 0:
		arr.extend(left)
	return arr


arr = [4, 6, 5, 7, 3, 1, 2]
arr = merge_sort(arr)
print(arr)
