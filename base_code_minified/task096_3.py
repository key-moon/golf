def p(A):
	J,H=len(A),len(A[0]);from collections import Counter as b,deque;c=b(B for A in A for B in A);K=c.most_common(1)[0][0];I=[[0]*H for A in A];L=[]
	for B in range(J):
		for C in range(H):
			if A[B][C]!=K and not I[B][C]:
				D=A[B][C];M=deque([(B,C)]);I[B][C]=1;N,O=[],[]
				while M:
					X,Y=M.popleft();N.append(X);O.append(Y)
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						F,G=X+P,Y+Q
						if 0<=F<J and 0<=G<H and not I[F][G]and A[F][G]==D:I[F][G]=1;M.append((F,G))
				R,S=min(N),max(N);T,U=min(O),max(O);L.append((D,R,S,T,U))
	d=J/2;e=H/2;L.sort(key=lambda F:(F[1]+F[2]<2*d,F[3]+F[4]<2*e));V=[]
	for(D,R,S,T,U)in L:W=[A[T+1:U]for A in A[R+1:S]];V.append((D,W))
	E=len(V[0][1]);Z=[[K]*(2*E+1)for A in range(2*E+1)]
	for(a,(D,W))in enumerate(V):
		P=a//2*(E+1);Q=a%2*(E+1)
		for B in range(E):
			for C in range(E):
				if W[B][C]!=K:Z[P+1+B][Q+1+C]=D
	return Z