def p(A):
	C={}
	for(D,Q)in enumerate(A):
		for(E,B)in enumerate(Q):
			if B:R,S,T,U=C.get(B,(15,15,0,0));C[B]=min(R,D),min(S,E),max(T,D),max(U,E)
	H=sorted(((A,*C[A])for A in C),key=lambda L:L[2]);V,W,X,Y,Z=H[0];a,b,c,d,e=H[1];f,g,h,i,j=H[2];F,J,G=Y-W+1,d-b+1,i-g+1;K,L,M=Z-X+1,e-c+1,j-h+1;N=1;O=15-M-1;I=min(15-max(F,G)-1,15-max(F,G)-J)//2;k=(N+K-1+O)//2;l=k-L//2;m=I+max(F,G);P=[[0]*15 for A in A]
	for(B,(n,o,p,q))in((V,(I,N,F,K)),(f,(I,O,G,M)),(a,(m,l,J,L))):
		for D in range(p):
			for E in range(q):P[n+D][o+E]=B
	return P