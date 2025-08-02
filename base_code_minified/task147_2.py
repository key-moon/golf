def p(A):
	J=0;K=[];E=set();L,M=len(A),len(A[0])
	for F in range(L):
		for G in range(M):
			if A[F][G]==3 and(F,G)not in E:
				B=[(F,G)];E.add((F,G))
				for(H,I)in B:
					for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=H+N,I+O
						if 0<=C<L and 0<=D<M and A[C][D]==3 and(C,D)not in E:E.add((C,D));B.append((C,D))
				if len(B)>J:J=len(B);K=B
	for(H,I)in K:A[H][I]=8
	return A