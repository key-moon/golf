def p(A):
	C=sum(A,[]);D=[A for A in set(C)if C.count(A)==1][0];B=[(B,E,A)for(B,C)in enumerate(A)for(E,A)in enumerate(C)if A and A!=D];E=(min(A for(A,B,C)in B)+max(A for(A,B,C)in B))//2;F=(min(A for(B,A,C)in B)+max(A for(B,A,C)in B))//2;G,H=next((A,C)for(A,B)in enumerate(A)for(C,E)in enumerate(B)if E==D);I,J=G-E,H-F
	for(K,L,M)in B:A[K+I][L+J]=M
	return A