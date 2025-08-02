def p(A):
	E,F=len(A),len(A[0]);G=lambda X:(X[1],-X[0]);I=[];N=[[0]*F for A in range(E)]
	for C in range(E):
		for D in range(F):
			if A[C][D]==4 and not N[C][D]:
				if D+1<F and A[C][D+1]==4:
					H=[];B=D
					while B<F and A[C][B]==4:N[C][B]=1;H.append((C,B));B+=1
					I.append((H,(0,1)))
				elif C+1<E and A[C+1][D]==4:
					H=[];B=C
					while B<E and A[B][D]==4:N[B][D]=1;H.append((B,D));B+=1
					I.append((H,(1,0)))
	O,J=I[0];U=len(O);K,L=G(J),(-G(J)[0],-G(J)[1]);V=[A[B+K[0]][C+K[1]]if 0<=B+K[0]<E and 0<=C+K[1]<F else 0 for(B,C)in O];W=[A[B+L[0]][C+L[1]]if 0<=B+L[0]<E and 0<=C+L[1]<F else 0 for(B,C)in O]
	for(X,M)in I:
		S=0;P=M
		for c in range(4):
			if P==J:break
			P=G(P);S+=1
		for(B,(Y,Z))in enumerate(X):
			for(d,(a,T))in enumerate(((V,G(M)),(W,(-G(M)[0],-G(M)[1])))):
				Q,R=Y+T[0],Z+T[1]
				if 0<=Q<E and 0<=R<F and A[Q][R]==0:b=B if S!=2 else U-1-B;A[Q][R]=a[b]
	return A