def p(A):
	H=len(A);I=len(A[0])
	for C in range(H):
		B=0
		while B<I:
			if A[C][B]==5:
				D=B
				while D<I and A[C][D]==5:D+=1
				if D-B>2:J,K,P=C,B,D-1;break
				B=D
			else:B+=1
		else:continue
		break
	R=max(B for B in range(J,H)if all(A[B][C]==5 for C in range(K,P+1)));L=[(B-(J+1),C-(K+1))for B in range(J+1,R)for C in range(K+1,P)if A[B][C]]
	if not L:return A
	S=A[J+1+L[0][0]][K+1+L[0][1]];M=set()
	for C in range(H):
		for B in range(I):
			if A[C][B]==1 and(C,B)not in M:
				Q=[(C,B)];M.add((C,B));G=[(C,B)]
				for(N,O)in Q:
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=N+T,O+U
						if 0<=E<H and 0<=F<I and A[E][F]==1 and(E,F)not in M:M.add((E,F));Q.append((E,F));G.append((E,F))
				V,W=min(A for(A,B)in G),min(A for(B,A)in G)
				if sorted((A-V,B-W)for(A,B)in G)==sorted(L):
					for(N,O)in G:A[N][O]=S
	return A