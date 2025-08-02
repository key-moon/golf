def p(g):
	from collections import deque;O,G=len(g),len(g[0]);H=[[0]*G for A in g];P=[]
	for I in range(O):
		for J in range(G):
			if g[I][J]and not H[I][J]:
				M=deque([(I,J)]);H[I][J]=1;Q=[]
				while M:
					A,B=M.popleft();Q.append((A,B))
					for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=A+T,B+U
						if 0<=C<O and 0<=D<G and g[C][D]and not H[C][D]:H[C][D]=1;M.append((C,D))
				P.append(Q)
	def R(p):A=[A for(A,B)in p];B=[A for(B,A)in p];return max(A)-min(A),max(B)-min(B)
	N=[A for A in P if R(A)[0]>R(A)[1]][0];K=[A for(A,B)in N];L=[A for(B,A)in N];X,Y,E=min(K),max(K),(min(K)+max(K))/2;Z,a,F=min(L),max(L),(min(L)+max(L))/2;V=[(A-E,B-F)for(A,B)in N];W=[(int(E+(B-F)),int(F-(A-E)))for(A,B)in V];S=[[0]*G for A in g]
	for(A,B)in W:S[A][B]=g[int(E+A-E)][int(F+B-F)]
	return S