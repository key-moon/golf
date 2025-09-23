def p(g):
	M=[A[:]for A in g];a,b=len(M),len(M[0]);A=[]
	for W in M:
		b=[]
		for X in W:b+=[X]*2
		A.extend([b[:],b[:]])
	J,K=len(A),len(A[0]);L=[[False]*K for A in range(J)];D=[]
	for B in range(J):
		for a in range(K):
			if A[B][a]!=2 or L[B][a]:continue
			O=[(B,a)];L[B][a]=True;P=[]
			while O:
				E,Q=O.pop();P.append((E,Q))
				for R in(-1,0,1):
					for S in(-1,0,1):
						if R==S==0:continue
						F,G=E+R,Q+S
						if 0<=F<J and 0<=G<K and not L[F][G]and A[F][G]==2:L[F][G]=True;O.append((F,G))
			D.append(P)
	Y={(B,a)for B in range(J)for a in range(K)if A[B][a]==2}
	def T(si,q,u,ej):
		for B in range(si,u+1):
			for a in range(q,ej+1):A[B][a]=4
	for E in D:H=[A for(A,B)in E];I=[A for(B,A)in E];T(min(H),min(I),max(H),max(I))
	def Z(A,B):
		a=10**9
		for(E,F)in A:
			for(G,H)in B:
				D=abs(E-G)+abs(F-H)
				if D<a:a=D
				if a==0:return 0
		return a
	d=len(D)
	for B in range(d):
		for a in range(d):
			if Z(D[B],D[a])<5:k=D[B]+D[a];H=[A for(A,B)in k];I=[A for(B,A)in k];T(min(H),min(I),max(H),max(I))
	for(B,a)in Y:A[B][a]=2
	return[A[::2]for A in A[::2]]