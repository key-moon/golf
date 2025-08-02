def p(g):
	L,H=len(g),len(g[0]);I=[[0]*H for A in g]
	for J in range(L):
		for K in range(H):
			if g[J][K]==0 and not I[J][K]:
				A=[(J,K)];I[J][K]=1
				for P in range(len(A)):
					M,N=A[P]
					for(Q,R)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=M+Q,N+R
						if 0<=B<L and 0<=C<H and g[B][C]==0 and not I[B][C]:I[B][C]=1;A.append((B,C))
				D=min(A for(A,B)in A);E=max(A for(A,B)in A);F=min(A for(B,A)in A);G=max(A for(B,A)in A);O=E-D
				if O==G-F and len(A)==(O+1)**2 and D and F and E<L-1 and G<H-1 and all(g[A][F-1]==5 for A in range(D,E+1))and all(g[A][G+1]==5 for A in range(D,E+1))and all(g[D-1][A]==5 for A in range(F,G+1))and all(g[E+1][A]==5 for A in range(F,G+1)):
					for(M,N)in A:g[M][N]=2
	return g