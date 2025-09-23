def p(I):
	J=True;Z,a=len(I),len(I[0])
	def K(G):return tuple(map(tuple,zip(*G)))
	def F(G):from collections import Counter as A;return A([B for A in G for B in A]).most_common(1)[0][0]
	def b(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
	def c(G,bg):
		F,H=len(G),len(G[0]);E=[[False]*H for A in range(F)];I=[]
		for A in range(F):
			for B in range(H):
				if E[A][B]or G[A][B]==bg:continue
				K=G[A][B];L=[(A,B)];E[A][B]=J;O=[]
				while L:
					M,N=L.pop()
					if G[M][N]!=K:continue
					O.append((M,N))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=M+P,N+Q
						if 0<=C<F and 0<=D<H and not E[C][D]and G[C][D]==K:E[C][D]=J;L.append((C,D))
				I.append((O,K))
		I.sort(key=lambda t:min(A for(A,B)in t[0]));return I
	def C(a,b):
		A,C=a;B,D=b
		if A==B:E,H=sorted((C,D));return{(A,B)for B in range(E,H+1)}
		if C==D:F,I=sorted((A,B));return{(A,C)for A in range(F,I+1)}
		if B-A==D-C:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E+A)for A in range(G+1)}
		if B-A==C-D:F,E=(A,C)if A<=B else(B,D);G=abs(B-A);return{(F+A,E-A)for A in range(G+1)}
		return set()
	def A(G,value,indices):
		D,E=len(G),len(G[0]);A=[list(A)for A in G]
		for(B,C)in indices:
			if 0<=B<D and 0<=C<E:A[B][C]=value
		return tuple(tuple(A)for A in A)
	def d(G,pairs):
		D,E=len(G),len(G[0]);A=[list(A)for A in G]
		for(F,(B,C))in pairs:
			if 0<=B<D and 0<=C<E:A[B][C]=F
		return tuple(tuple(A)for A in A)
	def e(indices):A=indices;B=[A for(A,B)in A];C=[A for(B,A)in A];D,E,F,G=min(B),min(C),max(B),max(C);return(D,E),(D,G),(F,E),(F,G)
	f=F(I);L=[(A,B)for A in range(Z)for B in range(a)if I[A][B]!=f]
	if L:g,h,i,j=b(L);G=i-g+1>j-h+1
	else:G=J
	H=tuple(tuple(A)for A in(I if G else K(I)));k=F(H);M=c(H,k);(l,N),(m,O)=M[0],M[-1];P=min(l);n=min(m);D=C(P,n);Q=max(1,len(D));o=sum(A for(A,B)in D)//Q;p=sum(A for(B,A)in D)//Q;B=o,p;q=C(P,B);r=A(H,O,D);E=A(r,N,q);R={(B[0],B[1]),(B[0]+1,B[1])};s,t=len(E),len(E[0]);S={(E[A][B],(A,B))for(A,B)in R if 0<=A<s and 0<=B<t};T={(A,(B,C+2))for(A,(B,C))in S}|{(A,(B,C-2))for(A,(B,C))in S};U={(A,B)for(C,(A,B))in T}
	if U:u,v,w,x=e(U);V={(A-1,B)for(A,B)in C(u,v)};W={(A+1,B)for(A,B)in C(w,x)}
	else:V=set();W=set()
	y=d(E,T);z=A(y,N,V);X=A(z,O,W);A0=F(X);Y=A(X,A0,R);return Y if G else K(Y)
