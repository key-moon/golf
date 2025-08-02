def p(g):
	A=len(g)
	if len({*sum(g,[])})<3:return[[g[B<A and B or 2*A-1-B][C<A and C or 2*A-1-C]for C in range(2*A)]for B in range(2*A)]
	B=lambda x:[list(A)for A in zip(*x[::-1])];return[A+B for(A,B)in zip(g,B(g))]+[A+B for(A,B)in zip(B(B(B(g))),B(B(g)))]