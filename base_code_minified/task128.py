def p(g):
	B={}
	for(C,P)in enumerate(g):
		for(D,A)in enumerate(P):
			if A:Q,R,S,T=B.get(A,(15,15,0,0));B[A]=min(Q,C),min(R,D),max(S,C),max(T,D)
	G=sorted(((A,*B[A])for A in B),key=lambda x:x[2]);U,V,W,X,Y=G[0];Z,a,b,c,d=G[1];e,f,h,i,j=G[2];E,I,F=X-V+1,c-a+1,i-f+1;J,K,L=Y-W+1,d-b+1,j-h+1;M=1;N=15-L-1;H=min(15-max(E,F)-1,15-max(E,F)-I)//2;k=(M+J-1+N)//2;l=k-K//2;m=H+max(E,F);O=[[0]*15 for A in g]
	for(A,(n,o,p,q))in((U,(H,M,E,J)),(e,(H,N,F,L)),(Z,(m,l,I,K))):
		for C in range(p):
			for D in range(q):O[n+C][o+D]=A
	return O