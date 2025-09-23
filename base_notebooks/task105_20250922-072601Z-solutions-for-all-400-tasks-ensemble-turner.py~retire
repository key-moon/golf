X=lambda g:list(zip(*g[::-1]))
def p(g,L=len,R=range):
	C=[A[:]for A in g]
	for M in R(4):
		g=X(g);C=[list(A)for A in X(C)];E,D=L(g),L(g[0]);F=[(A,B)for A in R(E)for B in R(D)if g[A][B]==1]
		if F:
			H,I,J,K=min(A for(A,B)in F),max(A for(A,B)in F),min(A for(B,A)in F),max(A for(B,A)in F)
			for A in R(E-1):
				for B in R(D-2):
					G=[B for B in R(D)if C[A][B]>0]
					if G and L(G)>3:
						if g[A][B]==1 and g[A][B+2]==1:C[A][B+1]=2
						if g[A][B]==1 and g[A+1][B+1]==1:C[A][B+1]=2
						if min(G)<B+1<max(G)and g[A][B+1]==0:C[A][B+1]=2
			for A in R(E):
				if A==H or A==I:
					for B in R(J,K+1):
						if C[A][B]==0:C[A][B]=2
			for B in R(D):
				if B==J or B==K:
					for A in R(H,I+1):
						if C[A][B]==0:C[A][B]=2
	E,D=L(g),L(g[0])
	for A in R(E):
		for B in R(D):
			if g[A][B]>0:C[A][B]=1
	return C