def p(A):
	D={};R,S=len(A),len(A[0])
	for T in range(R):
		for U in range(S):D.setdefault(A[T][U],set()).add((T,U))
	D.pop(0);V=sorted(D.items(),key=lambda H:len(H[1]));W,g=V[0][0],V[-1][0];X,Y=D[g],D[W]
	def Z(A):B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
	G,L,h,a=Z(X);H,m,M,n=h-G+1,a-L+1,0,0;b,c,i,j=Z(Y);I=i-b+1;J=j-c+1;k=[[1 if(G+A,L+B)in X else 0 for B in range(M)]for A in range(H)];l=[[1 if(b+A,c+B)in Y else 0 for B in range(J)]for A in range(I)];E,F=H*I,M*J;K=[[0]*F for A in range(E)]
	for B in range(H):
		for C in range(M):
			if k[B][C]:
				for d in range(I):
					for e in range(J):
						if l[d][e]:K[B*I+d][C*J+e]=W
	for(N,f)in((0,1),(1,0),(0,-1),(-1,0)):
		O=(G if N>=0 else G-E)+(N>0)*H+N-1;P=(a+1 if f>0 else L-F)+(f<0)*0
		if 0<=O<=R-E and 0<=P<=S-F:
			Q=1
			for B in range(E):
				for C in range(F):
					if K[B][C]and A[O+B][P+C]:Q=0;break
				if not Q:break
			if Q:
				for B in range(E):
					for C in range(F):
						if K[B][C]:A[O+B][P+C]=K[B][C]
				break
	return A