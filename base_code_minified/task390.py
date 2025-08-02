def p(A):
	H=[[0]*len(A)for B in A];E,B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==2],[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==5];I=min(A for(A,B)in E);J=max(A for(A,B)in E);K=min(A for(B,A)in E);L=max(A for(B,A)in E)
	if max(A for(B,A)in B)-min(A for(B,A)in B)>=max(A for(A,B)in B)-min(A for(A,B)in B):
		for(C,D)in B:F=D-K;G=L-D;H[C][K-F if F<=G else L+G]=5
	else:
		for(C,D)in B:F=C-I;G=J-C;H[I-F if F<=G else J+G][D]=5
	for(C,D)in E:H[C][D]=2
	return H