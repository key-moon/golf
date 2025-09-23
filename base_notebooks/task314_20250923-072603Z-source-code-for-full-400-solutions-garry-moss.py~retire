def X(grid):
	A={}
	for C in grid:
		for B in C:A[B]=A.get(B,0)+1
	return max(A,key=A.get)
def p(I):
	C,D=len(I),len(I[0]);R=X(I);N=[list(A)for A in I];E=[]
	for F in range(C):
		for G in range(D):
			H=I[F][G]
			if H==R:continue
			O=False
			for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
				P,Q=F+S,G+T
				if 0<=P<C and 0<=Q<D and I[P][Q]==H:O=True;break
			if not O:E.append((F,G,H))
	for(A,B,U)in E:
		for(J,K,V)in E:
			if A==J:L=(min(B,K)+max(B,K)+1)//2;M=A
			elif B==K:M=(min(A,J)+max(A,J)+1)//2;L=B
			else:continue
			if 0<=M<C and 0<=L<D:N[M][L]=U
	return N