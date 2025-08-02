def p(A):
	O,P=len(A),len(A[0]);C=[A[:]for A in A]
	for E in{B for A in A for B in A}-{0}:
		B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==E];F=min(A for(A,B)in B);F=F;Q=min(A for(B,A)in B);G=sum(A for(A,B)in B)/len(B);H=sum(A for(B,A)in B)/len(B);D=sorted(B,key=lambda R:-__import__('math').atan2(R[1]-H,R[0]-G));I=len(D)
		for(J,(K,L))in enumerate(D):M,N=D[(J+1)%I];C[M][N]=E;C[K][L]=0
	return C