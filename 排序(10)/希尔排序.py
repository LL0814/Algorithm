# -*- coding: utf-8 -*-

# 插入排序的优化版本
# 原因，如果较大值始终在较小值的之前，则较大值交换位置的次数将被放大
# 将数组按照 gap 分组
# 用插入排序对每一组排序，就可以将较小值交换到较大值之前
# gap 每一次 // 2，直到 gap 小于1为止
# 性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(1)  3、非稳定排序  4、原地排序

def shell_sort(arr):
	if (not isinstance(arr, list)) or len(arr) < 2:
		pass

	gap = len(arr) // 2
	while gap >= 1:
		for i in range(gap, len(arr)):
			j = i
			temp = arr[i]
			while j >= gap and temp < arr[j - gap]:
				arr[j] = arr[j - gap]
				j -= gap
			arr[j] = temp	
		gap = gap // 2

arr = [4, 6, 5, 7, 3, 1, 2]
shell_sort(arr)
print(arr)
