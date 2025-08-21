def p(j,A=enumerate):
	c=range;E=len(j);k=len(j[0]);W=lambda l,J:l==J or l*J<1;a=next((w for w in c(1,k)if all(W(b,K)for L in j for(b,K)in zip(L,L[w:]))),k);C=next((w for w in c(1,E)if all(W(b,K)for(w,L)in zip(j,j[w:])for(b,K)in zip(w,L))),E);e={}
	for(K,w)in A(j):
		for(L,b)in A(w):
			if b:e[K%C,L%a]=b
	for(K,w)in A(j):
		for(L,b)in A(w):
			if not b:w[L]=e[K%C,L%a]
	return j