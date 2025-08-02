def p(val_g):
	A={}
	for(C,K)in enumerate(val_g):
		for(D,E)in enumerate(K):
			if E:A.setdefault(E,[]).append((C,D))
	F=sorted(A,key=lambda val_k:len(A[val_k]));G,L=F[0],F[-1];B,M=A[L],A[G];H,N=min(A[0]for A in B),max(A[0]for A in B);I,O=min(A[1]for A in B),max(A[1]for A in B);P=(N-H+1)//3;Q=(O-I+1)//3;J=[[0]*3 for A in[None]*3]
	for(C,D)in M:J[(C-H)//P][(D-I)//Q]=G
	return J