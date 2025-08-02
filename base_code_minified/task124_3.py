def p(g):
	L,M=len(g),len(g[0]);E={(A,B)for A in range(L)for B in range(M)if g[A][B]}
	if not E:return g
	N=[(1,0),(-1,0),(0,1),(0,-1)];R=[A for A in E if sum((A[0]+B,A[1]+C)in E for(B,C)in N)==1];O,D=R;from collections import deque;G=deque([O]);H={O:None}
	while G:
		A=G.popleft()
		if A==D:break
		for(I,J)in N:
			F=A[0]+I,A[1]+J
			if F in E and F not in H:H[F]=A;G.append(F)
	B=[];A=D
	while A:B.append(A);A=H[A]
	B=B[::-1];P=[(B[A+1][0]-B[A][0],B[A+1][1]-B[A][1])for A in range(len(B)-1)];S=g[D[0]][D[1]];K=D;Q=0
	while True:
		I,J=P[Q%len(P)];C=K[0]+I,K[1]+J
		if not(0<=C[0]<L and 0<=C[1]<M):break
		if g[C[0]][C[1]]!=0:break
		g[C[0]][C[1]]=S;K=C;Q+=1
	return g