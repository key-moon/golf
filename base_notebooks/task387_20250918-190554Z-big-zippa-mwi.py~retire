ZERO=0
FIVE=5
def solve_f35d900a(I):
	L,M=len(I),len(I[0]);D=[list(A)for A in I];C,N=[],set()
	for A in range(L):
		for B in range(M):
			E=I[A][B]
			if E!=ZERO:C.append((A,B,E));N.add(E)
	if not C:return I
	F=sorted(N)
	def S(v):return F[0]if len(F)==1 or v==F[1]else F[1]
	for(A,B,E)in C:
		T=S(E)
		for O in(-1,0,1):
			for P in(-1,0,1):
				if O==0 and P==0:continue
				Q,R=A+O,B+P
				if 0<=Q<L and 0<=R<M:D[Q][R]=T
	G=min(A for(A,B,B)in C);H=max(A for(A,B,B)in C);J=min(B for(A,B,A)in C);K=max(B for(A,B,A)in C)
	if K>J:
		for B in range(J+1,K):
			if min(B-J,K-B)%2==0:D[G][B]=FIVE;D[H][B]=FIVE
	if H>G:
		for A in range(G+1,H):
			if min(A-G,H-A)%2==0:D[A][J]=FIVE;D[A][K]=FIVE
	return tuple(tuple(A)for A in D)
def p(g):A=tuple(tuple(A)for A in g);B=solve_f35d900a(A);return[list(A)for A in B]