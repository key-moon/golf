def p(A):
	C={(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==1}
	while C:
		J=C.pop();B={J};E=[J]
		while E:
			K,L=E.pop()
			for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
				D=K+M,L+N
				if D in C:C.remove(D);B.add(D);E.append(D)
		F,G=min(A for(A,B)in B),max(A for(A,B)in B);H,I=min(A for(B,A)in B),max(A for(B,A)in B);O={(F,A)for A in range(H,I+1)}|{(G,A)for A in range(H,I+1)}|{(A,H)for A in range(F,G+1)}|{(A,I)for A in range(F,G+1)}
		if B==O:
			for(P,Q)in B:A[P][Q]=8
	return A