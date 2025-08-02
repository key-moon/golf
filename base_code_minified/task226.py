def p(g):
	E=len(g);C=len(g[0]);J=[A for(A,B)in enumerate(g)if B.count(5)==C];K=[A for A in range(C)if all(g[B][A]==5 for B in range(E))];A=[-1]+J+[E];B=[-1]+K+[C];F=[(A[B]+1,A[B+1]-1)for B in range(len(A)-1)if A[B]+1<A[B+1]];G=[(B[A]+1,B[A+1]-1)for A in range(len(B)-1)if B[A]+1<B[A+1]];H=len(F);I=len(G)
	for D in range(3):
		L=D+1;M=(0,(H-1)//2,H-1)[D];N=(0,(I-1)//2,I-1)[D];O,P=F[M];Q,R=G[N]
		for S in range(O,P+1):
			for T in range(Q,R+1):g[S][T]=L
	return g