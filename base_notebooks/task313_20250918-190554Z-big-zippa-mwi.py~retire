def p(g,r=range,l=len):
	B=l(g);C=l(set(g[0]))-1;E=l({A[0]for A in g})-1
	for A in g:A[:]=(A[:C]*((l(A)-1)//C+1))[:l(A)]
	for D in r(B):g[D]=[g[D%E][A]for A in r(B)]
	return[[dict(zip(g[0],g[0][1:]))[A]for A in A]for A in g]