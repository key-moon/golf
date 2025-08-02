def p(g):
	Z='U';Y='D';X='L';W='R';C,F=len(g),len(g[0]);T=[A[:]for A in g];M=[A[:]for A in g]
	for a in set(A for B in g for A in B if A):
		N=[(A,B)for A in range(C)for B in range(F)if g[A][B]==a];D,G=min(A for(A,B)in N),max(A for(A,B)in N);E,H=min(A for(B,A)in N),max(A for(B,A)in N);Q=[[g[A][B]for B in range(E,H+1)]for A in range(D,G+1)];O,P=len(Q),len(Q[0])
		for(A,B)in N:M[A][B]=0
		I=F
		for A in range(D,G+1):
			for B in range(H+1,F):
				if M[A][B]:I=min(I,B-H-1);break
			else:I=min(I,F-H-1)
		J=F
		for A in range(D,G+1):
			for B in range(E-1,-1,-1):
				if M[A][B]:J=min(J,E-B-1);break
			else:J=min(J,E)
		K=C
		for B in range(E,H+1):
			for A in range(G+1,C):
				if M[A][B]:K=min(K,A-G-1);break
			else:K=min(K,C-G-1)
		L=C
		for B in range(E,H+1):
			for A in range(D-1,-1,-1):
				if M[A][B]:L=min(L,D-A-1);break
			else:L=min(L,D)
		dir=max((I,W),(J,X),(K,Y),(L,Z))[1]
		if{W:I,X:J,Y:K,Z:L}[dir]==0:continue
		b,c={W:(0,P),X:(0,-P),Y:(O,0),Z:(-O,0)}[dir];U=1
		while True:
			R,S=D+b*U,E+c*U
			if not(0<=R and R+O<=C and 0<=S and S+P<=F):break
			V=True
			for A in range(O):
				for B in range(P):
					if Q[A][B]and T[R+A][S+B]:V=False;break
				if not V:break
			if not V:break
			for A in range(O):
				for B in range(P):
					if Q[A][B]:T[R+A][S+B]=a
			U+=1
	for A in range(C):g[A][:]=T[A]
	return g