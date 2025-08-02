def p(A):
	J=[];K=1,0,-1,0,1
	for G in range(10):
		for H in range(10):
			if A[G][H]==5:
				I=[(G,H)];A[G][H]=0;B=[]
				while I:
					C,D=I.pop();B.append((C,D))
					for L in range(4):
						E=C+K[L];F=D+K[L+1]
						if 0<=E<10 and 0<=F<10 and A[E][F]==5:A[E][F]=0;I.append((E,F))
				J.append(B)
	for(B,M)in zip(sorted(J,key=len,reverse=True),(1,4,2)):
		for(C,D)in B:A[C][D]=M
	return A