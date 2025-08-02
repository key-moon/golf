def p(A):
	H=len(A);B=[(B,C,A[B][C])for B in range(H)for C in range(H)if A[B][C]];C=(min(A[0]for A in B)+max(A[0]for A in B))//2;D=(min(A[1]for A in B)+max(A[1]for A in B))//2
	for(E,F,G)in B:A[C-(F-D)][D+(E-C)]=G;A[2*C-E][2*D-F]=G;A[C+(F-D)][D-(E-C)]=G
	return A