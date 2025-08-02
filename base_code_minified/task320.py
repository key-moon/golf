def p(A):
	M,H=len(A),len(A[0]);D=[[0]*H for A in A]
	for E in range(M):
		for F in range(H):
			if A[E][F]==2 and not D[E][F]:
				I=[(E,F)];J=[];D[E][F]=1
				while I:
					N,G=I.pop();J.append((N,G))
					for(Q,R)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=N+Q,G+R
						if 0<=B<M and 0<=C<H and A[B][C]==2 and not D[B][C]:D[B][C]=1;I.append((B,C))
				O=[A for(A,B)in J];S,K=min(O),max(O);T=(K-S+1)//2;P=K-T+1
				for L in range(P,K+1):
					U=L-P+1;V=sorted(B for(A,B)in J if A==L)
					for G in V[:U]:A[L][G]=8
	return A