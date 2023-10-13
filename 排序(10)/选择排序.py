# -*- coding: utf-8 -*-

# 从第二项开始
# 将当前项与索引小于当前项的所有项依次比较，找到最小项的索引。
# 交换当前项与最小项的位置
# 性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、非稳定排序  4、原地排序

def selection_sort(arr):
	if (not isinstance(arr, list)) or len(arr) < 2:
		pass
	
	for i in range(len(arr) - 1):
		min_index = i
		for j in range(i + 1, len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j
		if i != min_index:
			arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [1, 4, 3, 5, 2]
selection_sort(arr)
print(arr)
