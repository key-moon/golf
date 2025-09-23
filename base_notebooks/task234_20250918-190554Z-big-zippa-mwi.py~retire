def p(g):
	S=None;T=len(g);U=len(g[0]);from collections import Counter as i;V=i(B for A in g for B in A);W=max(V,key=V.get);C={}
	for(A,j)in enumerate(g):
		for(B,I)in enumerate(j):
			if I!=W:C.setdefault(I,set()).add((A,B))
	if not C:return g
	def X(S):A=min(A for(A,B)in S);B=max(A for(A,B)in S);C=min(A for(B,A)in S);D=max(A for(B,A)in S);return A,B,C,D
	L=S;Y=S
	for(I,Z)in C.items():
		a,b,c,d=X(Z)
		if(b-a+1)*(d-c+1)==len(Z):L=I;Y=a,b,c,d;break
	if L is S or len(C)==1:return g
	M=next(A for A in C if A!=L);e=C[M];N=set()
	for(A,B)in e:
		k=(A-1,B-1),(A-1,B+1),(A+1,B-1),(A+1,B+1)
		if all(0<=A<T and 0<=B<U and g[A][B]==M for(A,B)in k):N.add((A,B))
	if not N:return g
	l,m,n,o=X(N);E,J,D,F=l-1,m+1,n-1,o+1;O=[A[:]for A in g]
	for(A,B)in e:O[A][B]=W
	P,f,K,Q=Y
	def R(a1,a2,b1,b2):return not(a2<b1 or a1>b2)
	p=R(D,F,K,Q);G=H=0;q=E+(J-E+1)//2;r=D+(F-D+1)//2;s=P+(f-P+1)//2;t=K+(Q-K+1)//2
	if p:G=1 if q<s else-1
	else:H=1 if r<t else-1
	def u(a,b):A,B,C,D=a;E,F,G,H=b;I=R(C,D,G,H)and(E-B==1 or A-F==1);J=R(A,B,E,F)and(G-D==1 or C-H==1);return I or J
	v=G;w=H;h=0
	while not u((E,J,D,F),(P,f,K,Q))and h<42:h+=1;E+=G;J+=G;D+=H;F+=H;v+=G;w+=H
	for A in range(max(0,E),min(T,J+1)):
		for B in range(max(0,D),min(U,F+1)):O[A][B]=M
	return O