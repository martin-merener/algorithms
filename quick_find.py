def quick_find(n, pairs):
	'''
	given n nodes, and a set of pairs between the nodes, quick_find returns the connected components of the graph
	'''
	I = list(range(n))
	for p in pairs:
		c0 = I[p[0]]
		c1 = I[p[1]]
		for k in range(n):
			if I[k]==c0:
				I[k]=c1
				print(I)
	return I

cc = quick_find(10, [(4,3),(3,8),(6,5),(9,4),(2,1),(5,0),(7,2),(6,1)]) 
print(cc)