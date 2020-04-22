

def matrix_mult_1(X,Y):
	''' O(n^3) '''
	l = len(X)
	if l == 1:
		return X*Y
	else:
		k = int(l/2)
		A = X[:k,:k]
		B = X[:k,k:]
		C = X[k:,:k]
		D = X[k:,k:]
		E = Y[:k,:k]
		F = Y[:k,k:]
		G = Y[k:,:k]
		H = Y[k:,k:]
		Z00 = matrix_mult_1(A,E)+matrix_mult_1(B,G)
		Z01 = matrix_mult_1(A,F)+matrix_mult_1(B,H)
		Z10 = matrix_mult_1(C,E)+matrix_mult_1(D,G)
		Z11 = matrix_mult_1(C,F)+matrix_mult_1(D,H)
		Z = np.empty((l,l))
		Z[:k,:k] = Z00
		Z[:k,k:] = Z01
		Z[k:,:k] = Z10
		Z[k:,k:] = Z11
		return Z

def matrix_mult_strassen(X,Y):
	l = len(X)
	if l == 1:
		return X*Y
	else:
		k = int(l/2)
		A = X[:k,:k]
		B = X[:k,k:]
		C = X[k:,:k]
		D = X[k:,k:]
		E = Y[:k,:k]
		F = Y[:k,k:]
		G = Y[k:,:k]
		H = Y[k:,k:]
		P1 = matrix_mult_strassen(A,F-H)
		P2 = matrix_mult_strassen(A+B,H)
		P3 = matrix_mult_strassen(C+D,E)
		P4 = matrix_mult_strassen(D,G-E)
		P5 = matrix_mult_strassen(A+D,E+H)		
		P6 = matrix_mult_strassen(B-D,G+H)
		P7 = matrix_mult_strassen(A-C,E+F)
		Z00 = P5+P4-P2+P6
		Z01 = P1+P2
		Z10 = P3+P4
		Z11 = P1+P5-P3-P7
		Z = np.empty((l,l))
		Z[:k,:k] = Z00
		Z[:k,k:] = Z01
		Z[k:,:k] = Z10
		Z[k:,k:] = Z11
		return Z


import numpy as np
import time


k = 8
n = 2**k
X = np.random.rand(n,n)
Y = np.random.rand(n,n)
#print(X)
#print(Y)

start_time = time.time()
Z0 = np.dot(X,Y)
print("--- %s seconds for numpy ---" % (time.time() - start_time))

start_time = time.time()
Z1 = matrix_mult_1(X,Y)
print("--- %s seconds for naive recursive ---" % (time.time() - start_time))

start_time = time.time()
Z2 = matrix_mult_strassen(X,Y)
print("--- %s seconds for strassen ---" % (time.time() - start_time))

E01 = abs(Z0-Z1)
E12 = abs(Z1-Z2)
print(np.max(E01), np.max(E12))