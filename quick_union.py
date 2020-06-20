def root(p, I):
	r = p
	while I[r]!=r:
		r = I[r]
	return r

#I = [0,9,6,5,4,2,6,1,0,5]
#print(root(3,I))
#print(root(7,I))

def quick_union(n, pairs):
	'''
	given n nodes, and a set of pairs between the nodes, quick_union returns the connected components of the graph
	'''
	I = list(range(n))
	for p in pairs:
		r_0 = root(p[0],I)
		r_1 = root(p[1],I)		
		if r_0!=r_1:
			I[r_0] = r_1
	R = [root(j,I) for j in I]		
	return R

cc = quick_union(10, [(4,3),(3,8),(6,5),(9,4),(2,1),(5,0),(7,2),(6,1)]) 
print(cc)

cc = quick_union(10, [(4,3),(3,8),(6,5),(9,4),(2,1),(5,4),(5,0),(7,2),(6,1),(7,3)]) 
print(cc)