def p(A):
	L,M=len(A),len(A[0]);C={(B,C)for B in range(L)for C in range(M)if A[B][C]}
	while C:
		B=[C.pop()]
		for Q in B:
			D,E=Q
			for(F,G)in((1,0),(-1,0),(0,1),(0,-1)):
				H=D+F,E+G
				if H in C:C.remove(H);B.append(H)
		if len(B)>1:
			I={}
			for(D,E)in B:I[A[D][E]]=I.get(A[D][E],0)+1
			for(N,R)in I.items():
				if R==1:break
			O,P=[(B,C)for(B,C)in B if A[B][C]==N][0];S=[(B-O,C-P,A[B][C])for(B,C)in B]
			for J in range(L):
				for K in range(M):
					if A[J][K]==N and(J,K)!=(O,P):
						for(F,G,T)in S:A[J+F][K+G]=T
	return A