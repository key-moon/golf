from collections import Counter,deque
def p(g):
	H,I=len(g),len(g[0]);M=Counter(B for A in g for B in A).most_common(1)[0][0];L=[A[:]for A in g];E=[[0]*I for A in range(H)]
	for A in range(H):
		for B in range(I):
			if g[A][B]!=M and not E[A][B]:
				N=g[A][B];J=deque([(A,B)]);E[A][B]=1;K=[]
				while J:
					F,G=J.popleft();K.append((F,G))
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=F+O,G+P
						if 0<=C<H and 0<=D<I and not E[C][D]and g[C][D]==N:E[C][D]=1;J.append((C,D))
				Q=2 if len(K)==6 else 1
				for(F,G)in K:L[F][G]=Q
	return L