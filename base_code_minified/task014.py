def p(A):
	B={}
	for(F,G)in enumerate(A):
		for D in G:
			if D and D not in B:B[D]=F
	E=max(B,key=B.get);C=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==E];H=min(A for(A,B)in C);I=max(A for(A,B)in C);J=min(A for(B,A)in C);K=max(A for(B,A)in C);return[[E if A[B][C]==E else 0 for C in range(J,K+1)]for B in range(H,I+1)]