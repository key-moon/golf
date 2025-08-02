def p(g):
	G={}
	for(A,K)in enumerate(g):
		for(B,E)in enumerate(K):
			if E:G.setdefault(E,[]).append((A,B))
	L,M=len(g),len(g[0])
	for(E,C)in G.items():
		if len(C)<2:continue
		for(J,N)in G.items():
			if J==E:continue
			F={A:[]for A in C}
			for(A,B)in N:O=min(C,key=lambda t:abs(A-t[0])+abs(B-t[1]));F[O].append((A,B))
			D=[A for A in C if F[A]]
			if len(D)==1 and len(F[D[0]])>1:
				P,Q=D[0];R=[(A-P,B-Q)for(A,B)in F[D[0]]]
				for(A,B)in C:
					if(A,B)!=D[0]:
						for(S,T)in R:
							H,I=A+S,B+T
							if 0<=H<L and 0<=I<M and g[H][I]==0:g[H][I]=J
	return g