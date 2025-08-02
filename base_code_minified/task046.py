import math
from collections import Counter
def p(g):
	g=[A[1:-1]for A in g];F,G=len(g),len(g[0]);B=[(A,B)for A in range(F)for B in range(G)if g[A][B]==5];H=Counter(A for B in g for A in B if A not in(0,5));K=min(H,key=lambda k:(H[k],k));L=sum(A for(A,B)in B)/len(B);M=sum(A for(B,A)in B)/len(B);B.sort(key=lambda p:math.atan2(p[1]-M,p[0]-L))
	def N(a,b,c):return(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
	A=[]
	for I in B+B[::-1]:
		while len(A)>1 and N(A[-2],A[-1],I)<=0:A.pop()
		A.append(I)
	A.pop()
	def O(i,j):
		B=j+.5;C=i+.5;D=0
		for((I,J),(K,L))in zip(A,A[1:]+A[:1]):E,F=I-C,J-B;G,H=K-C,L-B;D+=math.atan2(E*H-F*G,E*G+F*H)
		return abs(D)>1
	J=[]
	for D in range(F):
		C=[]
		for E in range(G):
			if g[D][E]==5:C.append(0)
			elif O(D,E):C.append(K)
			else:C.append(g[D][E])
		J.append(C)
	return J