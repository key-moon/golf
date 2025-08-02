def p(A):
	a='U';Z='D';Y='L';X='R';D,G=len(A),len(A[0]);U=[A[:]for A in A];N=[A[:]for A in A]
	for b in set(A for B in A for A in B if A):
		O=[(B,C)for B in range(D)for C in range(G)if A[B][C]==b];E,H=min(A for(A,B)in O),max(A for(A,B)in O);F,I=min(A for(B,A)in O),max(A for(B,A)in O);R=[[A[B][C]for C in range(F,I+1)]for B in range(E,H+1)];P,Q=len(R),len(R[0])
		for(B,C)in O:N[B][C]=0
		J=G
		for B in range(E,H+1):
			for C in range(I+1,G):
				if N[B][C]:J=min(J,C-I-1);break
			else:J=min(J,G-I-1)
		K=G
		for B in range(E,H+1):
			for C in range(F-1,-1,-1):
				if N[B][C]:K=min(K,F-C-1);break
			else:K=min(K,F)
		L=D
		for C in range(F,I+1):
			for B in range(H+1,D):
				if N[B][C]:L=min(L,B-H-1);break
			else:L=min(L,D-H-1)
		M=D
		for C in range(F,I+1):
			for B in range(E-1,-1,-1):
				if N[B][C]:M=min(M,E-B-1);break
			else:M=min(M,E)
		c=max((J,X),(K,Y),(L,Z),(M,a))[1]
		if{X:J,Y:K,Z:L,a:M}[c]==0:continue
		d,e={X:(0,Q),Y:(0,-Q),Z:(P,0),a:(-P,0)}[c];V=1
		while True:
			S,T=E+d*V,F+e*V
			if not(0<=S and S+P<=D and 0<=T and T+Q<=G):break
			W=True
			for B in range(P):
				for C in range(Q):
					if R[B][C]and U[S+B][T+C]:W=False;break
				if not W:break
			if not W:break
			for B in range(P):
				for C in range(Q):
					if R[B][C]:U[S+B][T+C]=b
			V+=1
	for B in range(D):A[B][:]=U[B]
	return A