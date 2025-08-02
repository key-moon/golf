def p(g):
	D={}
	for(B,J)in enumerate(g):
		for(C,E)in enumerate(J):
			if E:D.setdefault(E,[]).append((B,C))
	F=sorted(D.items(),key=lambda x:-len(x[1]));A=F[0][1];K=F[1][0];G,L=min(A for(A,B)in A),max(A for(A,B)in A);H,M=min(A for(B,A)in A),max(A for(B,A)in A);N=(L-G+1)//3;O=(M-H+1)//3;I=[[0]*3 for A in[0]*3]
	for(B,C)in A:I[(B-G)//N][(C-H)//O]=K
	return I