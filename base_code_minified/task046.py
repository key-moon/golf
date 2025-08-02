import math
from collections import Counter
def p(A):
	A=[A[1:-1]for A in A];G,H=len(A),len(A[0]);B=[(B,C)for B in range(G)for C in range(H)if A[B][C]==5];I=Counter(A for B in A for A in B if A not in(0,5));L=min(I,key=lambda L:(I[L],L));M=sum(A for(A,B)in B)/len(B);N=sum(A for(B,A)in B)/len(B);B.sort(key=lambda O:math.atan2(O[1]-N,O[0]-M))
	def O(A,B,C):return(B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
	C=[]
	for J in B+B[::-1]:
		while len(C)>1 and O(C[-2],C[-1],J)<=0:C.pop()
		C.append(J)
	C.pop()
	def P(A,B):
		C=B+.5;D=A+.5;E=0
		for((J,K),(L,M))in zip(HULL,HULL[1:]+HULL[:1]):F,G=J-D,K-C;H,I=L-D,M-C;E+=math.atan2(F*I-G*H,F*H+G*I)
		return abs(E)>1
	K=[]
	for E in range(G):
		D=[]
		for F in range(H):
			if A[E][F]==5:D.append(0)
			elif P(E,F):D.append(L)
			else:D.append(A[E][F])
		K.append(D)
	return K