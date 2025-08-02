def p(val_g):
	A=val_g;D=[B for A in A for B in A];G=max(D,key=D.count);M=[(1,0),(0,1),(-1,0),(0,-1)]
	def H(val_x):
		B={(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==val_x};F=[]
		while B:
			C={B.pop()};G=[]
			while C:
				D=C.pop();G.append(D)
				for H in M:
					E=D[0]+H[0],D[1]+H[1]
					if E in B:B.remove(E);C.add(E)
			F.append(G)
		return F
	for I in H(G):
		J=[A for(A,B)in I];K=[A for(B,A)in I];N,O=min(J),max(J);P,Q=min(K),max(K);B=[(B,C)for B in range(N,O+1)for C in range(P,Q+1)if A[B][C]==0]
		if not B:continue
		R,S=min(A for(A,B)in B),min(A for(B,A)in B);T=sorted((A-R,B-S)for(A,B)in B)
		for L in set(D)-{0,G}:
			for C in H(L):
				U,V=min(A for(A,B)in C),min(A for(B,A)in C)
				if sorted((A-U,B-V)for(A,B)in C)==T:
					for(E,F)in C:A[E][F]=0
					for(E,F)in B:A[E][F]=L
	return A