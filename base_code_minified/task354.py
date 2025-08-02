def p(g):
	H=set()
	for C in range(len(g)):
		for D in range(len(g[0])):
			if g[C][D]==5 and(C,D)not in H:
				I=[(C,D)];E=[(C,D)];H.add((C,D))
				while I:
					B,A=I.pop()
					for(F,G)in((B+1,A),(B-1,A),(B,A+1),(B,A-1)):
						try:
							if g[F][G]==5 and(F,G)not in H:H.add((F,G));I+=[(F,G)];E+=[(F,G)]
						except:0
				J=min(A for(A,B)in E);K=min(A for(B,A)in E);L=max(A for(B,A)in E)
				for A in range(K,L+1):
					if g[J-1][A]:M=g[J-1][A];break
				for(B,A)in E:g[B][A]=M
	return g