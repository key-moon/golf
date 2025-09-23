def p(g,L=len,R=range):
	E,F,C,D=L(g),L(g[0]),[],[]
	for A in R(E//2+1):
		for B in R(F):
			if g[A][B]==0:g[A][B]=g[-(A+1)][B];C+=[A];D+=[B]
			if g[-(A+1)][B]==0:g[-(A+1)][B]=g[A][B];C+=[E-(A+1)];D+=[B]
	for A in R(E):
		for B in R(F//2+1):
			if g[A][B]==0:g[A][B]=g[A][-(B+1)];C+=[A];D+=[B]
			if g[A][-(B+1)]==0:g[A][-(B+1)]=g[A][B];C+=[A];D+=[F-(B+1)]
	g=g[min(C):max(C)+1];g=[A[min(D):max(D)+1]for A in g];return g