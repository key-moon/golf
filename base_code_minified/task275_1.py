def p(A):
	from itertools import chain;B,N=len(A),len(A[0]);C=list(chain.from_iterable(A));G=max(set(C),key=C.count);D=[(B,C)for B in range(B)for C in range(N)if A[B][C]==G];O,P=min(A for(A,B)in D),min(A for(B,A)in D);E=[(A-O,B-P)for(A,B)in D];H=sorted({A for A in C if A and A!=G});I={B:A for(A,B)in enumerate(H)};J,K=max(A for(A,B)in E)+1,max(A for(B,A)in E)+1;L=[[0]*(len(H)*K)for A in range(B*J)]
	for M in range(B):
		for(V,F)in enumerate(A[M]):
			if F in I:
				Q=I[F];R=M*J;S=Q*K
				for(T,U)in E:L[R+T][S+U]=F
	return L