def p(A):
	S,M=len(A),len(A[0]);O=[[0]*M for A in A];W=[(1,0),(-1,0),(0,1),(0,-1)]
	def P(A,B,C):
		vis[A][B]=1;C.append((A,B))
		for(F,G)in N:
			D,E=A+F,B+G
			if 0<=D<h and 0<=E<w and not vis[D][E]and g[D][E]:P(D,E,C)
	B=[]
	for E in range(S):
		for F in range(M):
			if A[E][F]and not O[E][F]:
				D=[];P(E,F,D)
				if sum(A[B][C]==2 for(B,C)in D)>1:
					G=[A for(A,B)in D];K=[A for(B,A)in D];H,T,X,Y=min(G),min(K),max(G),max(K);B=[A[L:L+A]for A in A[H:H+U]]
					for(I,J)in D:A[I][J]=0
					U=1;break
		if B:break
	O=[[0]*M for A in A]
	for E in range(S):
		for F in range(M):
			if A[E][F]==2 and not O[E][F]:
				D=[];P(E,F,D);Q=[(B,C)for(B,C)in D if A[B][C]==2]
				if len(Q)<2:continue
				G=[A for(A,B)in Q];K=[A for(B,A)in Q]
				if len(set(G))==1:
					H=G[0];L,V=min(K),max(K);C=(V-L)//(len(B[0])-1)
					for I in range(len(B)):
						for J in range(len(B[0])):
							if B[I][J]==1:
								for N in range(C):
									for R in range(C):A[H+I*C+N][L+J*C+R]=1
				else:
					L=K[0];H,T=min(G),max(G);C=(T-H)//(len(B)-1)
					for I in range(len(B)):
						for J in range(len(B[0])):
							if B[I][J]==1:
								for N in range(C):
									for R in range(C):A[H+I*C+N][L+J*C+R]=1
	return A