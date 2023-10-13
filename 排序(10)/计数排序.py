# -*- coding: utf-8 -*-

# 计数排序是一种适合于最大值和最小值的差值不是不是很大的排序
# 就是把数组元素作为数组的下标，然后用一个临时数组统计该元素出现的次数，例如 temp[i] = m, 表示元素 i 一共出现了 m 次
# 最后再把临时数组统计的数据从小到大汇总起来，此时汇总起来是数据是有序的
# 引入 最小值 min 概念，减少空间复杂度
# 性质：1、时间复杂度：O(n+k)  2、空间复杂度：O(k)  3、稳定排序  4、非原地排序

def counting_sort(arr):
	temp = []
	max, min = arr[0], arr[0]
	for i in range(1, len(arr)):
		if max < arr[i]:
			max = arr[i]
		if min > arr[i]:
			min = arr[i]

	temp = [0] * (max - min + 1)

	for val in arr:
		temp[val - min] += 1

	arr = []
	for i in range(len(temp)):
		arr.extend([i + min] * temp[i])
	return arr

arr = [4, 6, -5, 7, 3, 1, 2]
arr = counting_sort(arr)
print(arr)