def p(g):
	C={}
	for(D,M)in enumerate(g):
		for(N,H)in enumerate(M):
			if H:C.setdefault(H,[]).append((D,N))
	A=next(A for(A,B)in C.items()if len(B)==4);I,J=zip(*C[A]);E,K=set(I),set(J);L,F=len(g),len(g[0]);B=[[0]*F for A in range(L)]
	if len(E)==2:
		for G in E:B[G]=[A]*F
	else:G=max(E,key=I.count);B[G]=[A]*F
	if len(K)>2:
		O=max(K,key=J.count)
		for D in range(L):B[D][O]=A
	return B