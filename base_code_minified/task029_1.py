def p(A):
	E={};F=0
	for(H,D)in enumerate(A):
		B=0
		while B<len(D):
			C=B+1
			while C<len(D)and D[C]==D[B]:C+=1
			if C-B>1:E.setdefault((B,C),[]).append(H)
			B=C
	for((B,C),G)in E.items():
		if len(G)==2 and C-B>F:F,I,J,K,L=C-B,C,B,*sorted(G)
	return[A[J+1:I-1]for A in A[K+1:L]]