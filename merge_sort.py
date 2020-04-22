def my_merge(list1, list2):
	'''Merge two already sorted (ascending) lists into one list'''
	j = 0
	k = 0
	merged = []
	while  j<len(list1) and k<len(list2):
		if list1[j]<=list2[k]:
			merged.append(list1[j])
			j = j+1
		else:
			merged.append(list2[k])
			k = k+1
	if j==len(list1):
		merged.extend(list2[k:])
	else:
		merged.extend(list1[j:])
	return merged

def my_merge_sort(a_list):
	if len(a_list)<2:
		return a_list
	else:
		k = int(len(a_list)/2)
		sorted_list1 = my_merge_sort(a_list[:k])
		sorted_list2 = my_merge_sort(a_list[k:])
		sorted_list = my_merge(sorted_list1, sorted_list2)
		return sorted_list

import random
n = 100
randomlist = random.sample(range(0, 1000), n)
sorted_list = my_merge_sort(randomlist)
print(randomlist)
print(sorted_list)
