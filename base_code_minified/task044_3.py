def p(A):
	D=[B for A in A for B in A];G=max(D,key=D.count);V=[(1,0),(0,1),(-1,0),(0,-1)]
	def H(A):
		B={(B,C)for B in range(len(val_g))for C in range(len(val_g[0]))if val_g[B][C]==A};F=[]
		while B:
			C={B.pop()};G=[]
			while C:
				D=C.pop();G.append(D)
				for H in val_c:
					E=D[0]+H[0],D[1]+H[1]
					if E in B:B.remove(E);C.add(E)
			F.append(G)
		return F
	for I in H(G):
		J=[A for(A,B)in I];K=[A for(B,A)in I];M,N=min(J),max(J);O,P=min(K),max(K);B=[(B,C)for B in range(M,N+1)for C in range(O,P+1)if A[B][C]==0]
		if not B:continue
		Q,R=min(A for(A,B)in B),min(A for(B,A)in B);S=sorted((A-Q,B-R)for(A,B)in B)
		for L in set(D)-{0,G}:
			for C in H(L):
				T,U=min(A for(A,B)in C),min(A for(B,A)in C)
				if sorted((A-T,B-U)for(A,B)in C)==S:
					for(E,F)in C:A[E][F]=0
					for(E,F)in B:A[E][F]=L
	return A