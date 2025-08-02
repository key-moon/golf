def p(A):
	G=sum(A,[]);I=max(set(G),key=G.count)
	for H in set(G)-{I}:
		B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==H]
		if(C:=max(A for(A,B)in B)-min(A for(A,B)in B)+1)*(D:=max(A for(B,A)in B)-min(A for(B,A)in B)+1)>len(B):K,L=min(A for(A,B)in B),min(A for(B,A)in B);break
	J=[(A,B)for A in range(C)for B in range(D)if A*(A-C+1)*B*(B-D+1)==0]
	for E in range(len(A)-C+1):
		for F in range(len(A[0])-D+1):
			if E==K and F==L:continue
			if all(A[E+B][F+C]==I for B in range(1,C-1)for C in range(1,D-1))and all(A[E+B][F+C]!=H for(B,C)in J):
				for(M,N)in J:A[E+M][F+N]=H
				return A
	return A