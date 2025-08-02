def p(A):
	H,I=len(A),len(A[0]);D=set();J=[]
	for E in range(H):
		for F in range(I):
			if A[E][F]and(E,F)not in D:
				G=[(E,F)];D.add((E,F))
				for K in G:
					for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=K[0]+N,K[1]+O
						if 0<=B<H and 0<=C<I and A[B][C]and(B,C)not in D:D.add((B,C));G.append((B,C))
				J.append(G)
	P=max(J,key=lambda H:(len(H),max(H)[0]));L,M=zip(*P);return[[A[B][C]for C in range(min(M),max(M)+1)]for B in range(min(L),max(L)+1)]