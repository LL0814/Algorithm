# -*- coding: utf-8 -*-

# 从第二项开始
# 记录当前项的值
# 将当前项与索引小于当前项的所有项倒序依次比较，找到最小项的索引。
# 从最小项索引+1 开始，到当前项结束，将所有项的值依次赋值为前一项的值
# 将最小项的值赋值为当前项的值
# 性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

def insertion_sort(arr):
	if (not isinstance(arr, list)) or len(arr) < 2:
		pass
	
	for i in range(1, len(arr)):
		temp = arr[i]
		k = i - 1 # 不与自己比较
		while k >= 0 and arr[k] > temp:
			arr[k + 1] = arr[k] #依次往后位移一位
			k -= 1
		arr[k + 1] = temp

arr = [4, 3, 1, 5, 2]
insertion_sort(arr)
print(arr)