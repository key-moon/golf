def p(g):
	G=len(g);A=[(A,B,g[A][B])for A in range(G)for B in range(G)if g[A][B]];B=(min(A[0]for A in A)+max(A[0]for A in A))//2;C=(min(A[1]for A in A)+max(A[1]for A in A))//2
	for(D,E,F)in A:g[B-(E-C)][C+(D-B)]=F;g[2*B-D][2*C-E]=F;g[B+(E-C)][C-(D-B)]=F
	return g