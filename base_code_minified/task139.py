def p(g):
	M,N=len(g),len(g[0]);G=set()
	for E in range(M):
		for F in range(N):
			if g[E][F]==4 and(E,F)not in G:
				H=[(E,F)];G.add((E,F));I=J=E;K=L=F
				while H:
					A,B=H.pop()
					if A<I:I=A
					if A>J:J=A
					if B<K:K=B
					if B>L:L=B
					for(C,D)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
						if 0<=C<M and 0<=D<N and g[C][D]==4 and(C,D)not in G:G.add((C,D));H.append((C,D))
				for C in range(I,J+1):
					for D in range(K,L+1):
						if g[C][D]==0:g[C][D]=7
	return g