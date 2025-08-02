def p(A):
	B=[(B,C,A[B][C])for B in range(10)for C in range(10)if A[B][C]];G=(min(A for(A,B,C)in B)+max(A for(A,B,C)in B))//2;H=(min(A for(B,A,C)in B)+max(A for(B,A,C)in B))//2
	for(C,D,I)in B:E=2*G-C;F=2*H-D;A[C][F]=A[E][D]=A[E][F]=I
	return A