def p(g):
	d=None;N=False;c,Q=len(g),len(g[0]);from collections import Counter as T;R=T(B for A in g for B in A);A=min(R,key=R.get);F=[(B,r)for B in range(c)for r in range(Q)if g[B][r]==A]
	if not F:return[A[:]for A in g]
	U=min(A for(A,B)in F);m=min(A for(B,A)in F);o=max(A for(A,B)in F);l=max(A for(B,A)in F);D=o-U+1;y=l-m+1;p=max(1,D-2);e=max(1,y-2)
	def a(i,j):
		for B in range(j,j+y):
			if g[i][B]!=A or g[i+D-1][B]!=A:return N
		for r in range(i,i+D):
			if g[r][j]!=A or g[r][j+y-1]!=A:return N
		return True
	G=d
	for B in range(c-(p+2)+1):
		for r in range(Q-(e+2)+1):
			M=True
			for I in range(B+1,B+p+1):
				o=g[I]
				for J in range(r+1,r+e+1):
					if o[J]!=0:M=N;break
				if not M:break
			if M:
				if G is d or a(*G)and not a(B,r):G=B,r
	if G is d:return[A[:]for A in g]
	B,r=G;D=p+2;y=e+2;H=[A[:]for A in g]
	for J in range(r,r+y):H[B][J]=A;H[B+D-1][J]=A
	for I in range(B,B+D):H[I][r]=A;H[I][r+y-1]=A
	return H