def p(g):
	N='h';J,D=len(g),len(g[0]);S=[[not g[A][B]and all(not(0<=A+C<J and 0<=B+E<D)or not g[A+C][B+E]for C in(-1,0,1)for E in(-1,0,1)if C or E)for B in range(D)]for A in range(J)];K=[0]*D;E=[]
	for O in range(J):
		for P in range(D):K[P]=S[O][P]and K[P]+1
		for L in range(D):
			C=K[L]
			if C:
				for B in range(L,D):
					if not K[B]:break
					C=min(C,K[B]);[E.append((O-A+1,L,O,B,(B-L+1)*A))for A in range(1,C+1)]
	if not E:return[[*A]for A in g]
	F,I=lambda x:x[3]-x[1]+1,lambda x:x[2]-x[0]+1;E.sort(key=lambda r:(-r[4],r[0],r[1]));G=next((A for A in E if F(A)>I(A)),0);H=next((A for A in E if I(A)>F(A)),0);A=G and H and(G if F(G)>I(H)else H if F(G)<I(H)else G if G[4]>=H[4]else H)or G or H or E[0];M=[[*A]for A in g]
	def Q(a):
		for A in range(a[0],a[2]+1):M[A][a[1]:a[3]+1]=[3]*F(a)
	T=lambda a,b:a[1]<=b[3]and b[1]<=a[3]and a[0]<=b[2]and b[0]<=a[2];C='vh'[F(A)<=I(A)];U=lambda a:a[1]==0 or a[3]==D-1 if C==N else a[0]==0 or a[2]==J-1;V=lambda a:(a[3]+1==A[1]or a[1]-1==A[3])and a[0]<=A[2]and a[2]>=A[0]if C==N else(a[2]+1==A[0]or a[0]-1==A[2])and a[1]<=A[3]and a[3]>=A[1];W=lambda a:all(not(0<=A<J and 3 in M[A][a[1]:a[3]+1])for A in(a[0]-1,a[2]+1))if C==N else all(not(0<=A<D and 3 in[*zip(*M[a[0]:a[2]+1])][A])for A in(a[1]-1,a[3]+1));Q(A);R=[A]
	while 1:
		for B in sorted(E,key=lambda r:(not U(r),-r[4],r[0],r[1])):
			if(F,I)[C>N](B)<5 or not W(B)or not V(B)or any(T(B,A)for A in R):continue
			Q(B);R+=[B];break
		else:break
	return M