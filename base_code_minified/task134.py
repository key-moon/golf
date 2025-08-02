def p(A):
	E={}
	for(C,K)in enumerate(A):
		for(D,F)in enumerate(K):
			if F:E.setdefault(F,[]).append((C,D))
	G=sorted(E.items(),key=lambda H:-len(H[1]));B=G[0][1];L=G[1][0];H,M=min(A for(A,B)in B),max(A for(A,B)in B);I,N=min(A for(B,A)in B),max(A for(B,A)in B);O=(M-H+1)//3;P=(N-I+1)//3;J=[[0]*3 for A in[0]*3]
	for(C,D)in B:J[(C-H)//O][(D-I)//P]=L
	return J