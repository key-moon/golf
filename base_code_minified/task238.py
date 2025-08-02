def p(g):
	D={}
	for(N,O)in enumerate(g):
		for(P,A)in enumerate(O):
			if A:D.setdefault(A,[]).append([N,P])
	B=[];C=[]
	for(E,J)in D.items():
		K=[A for(A,B)in J];L=[A for(B,A)in J];F,G=min(K),min(L);H=max(K)-F+1;M=max(L)-G+1
		if H>1 and M>1:A,Q,R,S,I=E,F,G,H,M
		elif H==1:B.append((F,E))
		else:C.append((G,E))
	B.sort();C.sort();T=B[0][1];U=B[-1][1];V=C[0][1];W=C[-1][1];return[[0]+[T]*I+[0]]+[[V]+[A if[B+Q,C+R]in D[A]else 0 for C in range(I)]for B in range(S)]+[[0]+[U]*I+[0]]