def p(g):
	G={};L,M=len(g),len(g[0])
	for C in range(L):
		for D in range(M):
			H=g[C][D]
			if H:
				I=C;J=D;g[C][D]=0;K=[(C,D)]
				while K:
					A,B=K.pop()
					if A<I:I=A
					if B<J:J=B
					for(E,F)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
						if 0<=E<L and 0<=F<M and g[E][F]==H:g[E][F]=0;K.append((E,F))
				G.setdefault(I,[]).append((J,H))
	return[[A for(B,A)in sorted(G[A])]for A in sorted(G)]