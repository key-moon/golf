j=len
A=range
def p(c):
	c=[W[:]+W[:]for W in c]+[W[:]+W[:]for W in c];E,k=j(c),j(c[0])
	for W in A(E):
		for l in A(k):
			J=c[W][l]
			if J>0 and J!=8:
				for(a,C)in[[1,1],[-1,-1],[-1,1],[1,-1]]:
					if a+W>=0 and C+l>=0 and a+W<E and C+l<k:
						if c[a+W][C+l]==0:c[a+W][C+l]=8
	return c