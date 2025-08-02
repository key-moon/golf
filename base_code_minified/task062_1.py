def p(g):
	A=range;k={A for B in g for A in B if A};D,E=sorted(k,key=lambda c:max(A for B in g for A in B if A==c)/min(A for B in g for A in B if A==c)if False else 0)
	def W(c):A=[A for(A,B)in enumerate(g)for(D,C)in enumerate(B)if C==c];B=[B for(D,A)in enumerate(g)for(B,C)in enumerate(A)if C==c];return min(A),max(A),min(B),max(B)
	F,G,H,I=W(D);J=G-F+1;K=I-H+1;L,M,N,O=W(E);P=M-L+1;Q=O-N+1
	if K*P>=J*Q:X,l,m,Y,Z,R,a=D,F,G,H,I,J,K;b,c,d,n,o,e,S=E,L,M,N,O,P,Q
	else:X,l,m,Y,Z,R,a=E,L,M,N,O,P,Q;b,c,d,n,o,e,S=D,F,G,H,I,J,K
	T=a+e;U=R+S;f=(c+d)//2;h=(Y+Z)//2;V=[[3]*10 for A in A(10)];i=(R-1)//2
	for p in A(-i,i+1):
		B=f+p
		if 0<=B<10:
			for q in A(-T//2,T-T//2):
				C=h+q
				if 0<=C<10:V[B][C]=X
	j=(S-1)//2
	for r in A(-j,j+1):
		C=h+r
		if 0<=C<10:
			for s in A(-U//2,U-U//2):
				B=f+s
				if 0<=B<10:V[B][C]=b
	return V