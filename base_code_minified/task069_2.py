def p(A):
	B,C=len(A),len(A[0]);E={}
	for L in range(B):
		for M in range(C):
			D=A[L][M]
			if D:E[D]=E.get(D,0)+1
	I=max(E,key=E.get);F=[(B,E,A[B][E])for B in range(B)for E in range(C)if(D:=A[B][E])and D!=I];N=min(A for(A,B,C)in F);O=min(A for(B,A,C)in F);J=[(A-N,B-O,C)for(A,B,C)in F];K=[[0]*C for A in range(B)]
	for G in range(B):
		for H in range(C):
			if all(0<=G+D<B and 0<=H+E<C and A[G+D][H+E]==I for(D,E,F)in J):
				for(P,Q,R)in J:K[G+P][H+Q]=R
	return K