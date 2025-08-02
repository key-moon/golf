def p(g):
	N,L=len(g),len(g[0]);M=[[0]*L for A in g];T=[(1,0),(-1,0),(0,1),(0,-1)]
	def O(i,j,c):
		M[i][j]=1;c.append((i,j))
		for(C,D)in T:
			A,B=i+C,j+D
			if 0<=A<N and 0<=B<L and not M[A][B]and g[A][B]:O(A,B,c)
	A=[]
	for D in range(N):
		for E in range(L):
			if g[D][E]and not M[D][E]:
				C=[];O(D,E,C)
				if sum(g[A][B]==2 for(A,B)in C)>1:
					F=[A for(A,B)in C];J=[A for(B,A)in C];G,S,V,W=min(F),min(J),max(F),max(J);A=[A[K:K+X]for A in g[G:G+Y]]
					for(H,I)in C:g[H][I]=0
					Z=1;break
		if A:break
	M=[[0]*L for A in g]
	for D in range(N):
		for E in range(L):
			if g[D][E]==2 and not M[D][E]:
				C=[];O(D,E,C);P=[(A,B)for(A,B)in C if g[A][B]==2]
				if len(P)<2:continue
				F=[A for(A,B)in P];J=[A for(B,A)in P]
				if len(set(F))==1:
					G=F[0];K,U=min(J),max(J);B=(U-K)//(len(A[0])-1)
					for H in range(len(A)):
						for I in range(len(A[0])):
							if A[H][I]==1:
								for Q in range(B):
									for R in range(B):g[G+H*B+Q][K+I*B+R]=1
				else:
					K=J[0];G,S=min(F),max(F);B=(S-G)//(len(A)-1)
					for H in range(len(A)):
						for I in range(len(A[0])):
							if A[H][I]==1:
								for Q in range(B):
									for R in range(B):g[G+H*B+Q][K+I*B+R]=1
	return g