def p(A):
	G,H=len(A),len(A[0]);K=set();I=set()
	for B in range(G):
		for C in range(H):
			if A[B][C]and(B,C)not in K:
				J=[(B,C)];D={(B,C)}
				while J:
					N,O=J.pop()
					for L in(-1,0,1):
						for M in(-1,0,1):
							if L|M:
								E,F=N+L,O+M
								if 0<=E<G and 0<=F<H and A[E][F]and(E,F)not in D:D.add((E,F));J.append((E,F))
				K|=D
				if len(D)>len(I):I=D
	for B in range(G):
		for C in range(H):
			if A[B][C]and(B,C)not in I:A[B][C]=0
	return A