def p(g):
	E=set();J=len(g);K=len(g[0])
	for C in range(J):
		for D in range(K):
			if g[C][D]and(C,D)not in E:
				F=[(C,D)];G=[(C,D)];E.add((C,D))
				while G:
					H,I=G.pop()
					for(O,P)in((1,0),(0,1),(-1,0),(0,-1)):
						B,A=H+O,I+P
						if 0<=B<J and 0<=A<K and g[B][A]and(B,A)not in E:E.add((B,A));G+=[(B,A)];F+=[(B,A)]
				L,A=zip(*F);M,N=max(L)-min(L)+1,max(A)-min(A)+1
				if M>1 and N>1 and len(F)==2*(M+N)-4:
					for(H,I)in F:g[H][I]=3
	return g