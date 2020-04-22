

'''
Input: array A containing the numbers 1,...,n in some arbitrary order.
Output: number of inversions in the list: that is the number of pairs (i,j) such that A[i]>A[j]

One usage is to have a similarity measure between two rankings
'''

def count_inversions0(A):
	C = 0
	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i]>A[j]:
				C = C+1
	return C

def counting_inversions(A):
	if len(A)<2:
		return A,0
	else:
		k = int(len(A)/2)
		sorted_list1, C1 = counting_inversions(A[:k])
		sorted_list2, C2 = counting_inversions(A[k:])
		sorted_list, C3 = merge(sorted_list1, sorted_list2)
		return sorted_list, C1+C2+C3	

def merge(list1, list2):
	'''Merge two already sorted (ascending) lists into one list, and count split inversions'''
	j = 0
	k = 0
	C = 0
	merged = []
	while  j<len(list1) and k<len(list2):
		if list1[j]<=list2[k]:
			merged.append(list1[j])
			j = j+1
		else:
			merged.append(list2[k])
			k = k+1
			C = C + len(list1)-j
	if j==len(list1):
		merged.extend(list2[k:])
	else:
		merged.extend(list1[j:])
	return merged, C

import random
n = 10
randomlist = random.sample(range(0, 1000), n)
print(randomlist)
sorted_list, C = counting_inversions(randomlist)
D = count_inversions0(randomlist)
print(sorted_list)
print(C,D)
