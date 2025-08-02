def p(A):
	L=len(A);M=len(A[0]);G=set()
	for H in range(L):
		for I in range(M):
			if A[H][I]!=8 and(H,I)not in G:
				J=[(H,I)];N=[];D={};G.add((H,I))
				while J:
					B,C=J.pop();N.append((B,C));K=A[B][C]
					if K>0 and K not in D:D[K]=B,C
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=B+P,C+Q
						if 0<=E<L and 0<=F<M and A[E][F]!=8 and(E,F)not in G:G.add((E,F));J.append((E,F))
				if len(D)==2:
					O,R=sorted(D);S,T=D[O];U=S+T&1
					for(B,C)in N:A[B][C]=O if B+C&1==U else R
	return A