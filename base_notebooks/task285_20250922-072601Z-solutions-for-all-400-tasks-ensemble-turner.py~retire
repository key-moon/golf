from collections import deque,Counter
def p(g):
	S=None;T=lambda p:Counter([B for A in p for B in A]if isinstance(p,list)and p and isinstance(p[0],list)else[A for(A,B)in p]).most_common(1)[0][0]if p else 0
	def e(G,d=1,b=1):
		E,F=len(G),len(G[0]);K=T(G)if b else S;D=[[0]*F for A in range(E)];N=[];O=(lambda i,j:[(i+A,j+B)for A in(-1,0,1)for B in(-1,0,1)if A or B])if d else lambda i,j:[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
		for H in range(E):
			for I in range(F):
				if D[H][I]or b and G[H][I]==K:D[H][I]=1;continue
				L=deque([(H,I)]);M=[]
				while L:
					A,B=L.popleft()
					if not(0<=A<E and 0<=B<F)or D[A][B]:continue
					C=G[A][B]
					if b and C==K:D[A][B]=1;continue
					D[A][B]=1;M.append((C,(A,B)))
					for(J,C)in O(A,B):
						if 0<=J<E and 0<=C<F and not D[J][C]and(not b or G[J][C]!=K):L.append((J,C))
				if M:N.append(M)
		return N
	I=lambda p:[A for(B,A)in p];A=lambda I:(min(A for(A,B)in I),min(A for(B,A)in I),max(A for(A,B)in I),max(A for(B,A)in I));f=lambda I:(A(I)[2]-A(I)[0]+1,A(I)[3]-A(I)[1]+1);U=lambda I:(A(I)[0]+(A(I)[2]-A(I)[0])//2,A(I)[1]+(A(I)[3]-A(I)[1])//2)
	def h(a,b):
		A,B=U(a);C,D=U(b)
		if A==C:return 0,1 if B<D else-1
		if B==D:return 1 if A<C else-1,0
		if A<C:return 1,1 if B<D else-1
		if A>C:return-1,1 if B<D else-1
		return 0,0
	def i(l,O):A,B=l;C=set(O);return any((A,B)in C for(A,B)in((A-1,B),(A+1,B),(A,B-1),(A,B+1)))
	V=lambda p:[(B,(A(I(p))[0]+A(I(p))[2]-C,D))for(B,(C,D))in p]if p else[];W=lambda p:[(B,(C,A(I(p))[1]+A(I(p))[3]-D))for(B,(C,D))in p]if p else[];D=lambda p,d:[(A,(B+d[0],C+d[1]))for(A,(B,C))in p]
	def L(G,C):
		F,H=len(G),len(G[0]);A=[A[:]for A in G]
		for(B,(D,E))in C:
			if B and 0<=D<F and 0<=E<H:A[D][E]=B
		return A
	def M(G,I):
		for(A,B)in I:
			C=G[A][B]
			if C:return C
		for(A,B)in I:return G[A][B]
		return 0
	g=[list(A)for A in g];j=e(g);C=[A[:]for A in g];N,O,P=[],[],[]
	for B in j:
		if not B:continue
		E=T(B);X=[A for A in B if A[0]==E];k=[A for A in B if A[0]!=E];Y=[A for(B,A)in X];G=[A for(B,A)in k];H=S
		for Q in B:
			if Q[0]==E and i(Q[1],G):H=Q;break
		if H is S:H=X[0]
		l=G+[H[1]]if G else[H[1]];m,n,o,p=A(l);R={(A,B)for A in range(m,o+1)for B in range(n,p+1)};J,K=h(Y,G if G else Y);Z,a=f([A for(B,A)in B]);q,r,s=(Z*J,0),(0,a*K),(Z*J,a*K)
		def F(v):v=-v;return 0 if v==0 else v+1 if v>0 else v-1
		t,u,v=(F(J),F(0)),(F(0),F(K)),(F(J),F(K));w=[A for A in D(V(B),q)if A[0]==E];x=[A for A in D(W(B),r)if A[0]==E];y=[A for A in D(V(W(B)),s)if A[0]==E];b,c,d=D(w,t),D(x,u),D(y,v);N+=[(M(g,{A for(B,A)in b if A in R}),A)for(B,A)in b];O+=[(M(g,{A for(B,A)in c if A in R}),A)for(B,A)in c];P+=[(M(g,{A for(B,A)in d if A in R}),A)for(B,A)in d]
	if N:C=L(C,N)
	if O:C=L(C,O)
	if P:C=L(C,P)
	return C