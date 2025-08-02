def p(g):
	H=set();N=[];O=[];P,Q=len(g),len(g[0])
	for E in range(P):
		for F in range(Q):
			L=g[E][F]
			if L==1 and(E,F)not in H:
				G=I=E;J=K=F;M=[(E,F)];H.add((E,F))
				while M:
					C,D=M.pop()
					if C<G:G=C
					if C>I:I=C
					if D<J:J=D
					if D>K:K=D
					for R in(1,-1):
						A,B=C+R,D
						if 0<=A<P and g[A][B]==1 and(A,B)not in H:H.add((A,B));M.append((A,B))
						A,B=C,D+R
						if 0<=B<Q and g[A][B]==1 and(A,B)not in H:H.add((A,B));M.append((A,B))
				N.append((G,I,J,K))
			elif L>1:O.append((E,F,L))
	for(E,F,L)in O:
		for(G,I,J,K)in N:
			if G<=E<=I and J<=F<=K:
				S=G-1 if G else 0
				for C in range(S,I+1):
					for D in range(J,K+1):
						if g[C][D]==0:g[C][D]=L
				break
	return g