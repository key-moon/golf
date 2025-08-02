def p(g):
	J=len(g);K=len(g[0]);E=set();L=[];M=0
	for F in range(J):
		for G in range(K):
			if g[F][G]==0 and(F,G)not in E:
				I=[(F,G)];E.add((F,G));H=[]
				while I:
					A,B=I.pop();H.append((A,B))
					for N in(1,-1):
						for(C,D)in((A+N,B),(A,B+N)):
							if 0<=C<J and 0<=D<K and g[C][D]==0 and(C,D)not in E:E.add((C,D));I.append((C,D))
				if len(H)>M:M,L=len(H),H
	for(A,B)in L:g[A][B]=3
	return g