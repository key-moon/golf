def p(g):
	f=False;I=True;B,C=len(g),len(g[0]);T=[B for A in g for B in A];J=max(set(T),key=T.count)
	def G(i,j):return 0<=i<B and 0<=j<C
	def h():
		E=[[f]*C for A in range(B)];L=[]
		for F in range(B):
			for H in range(C):
				if E[F][H]or g[F][H]==J:continue
				K,M=[(F,H)],set();E[F][H]=I
				while K:
					N,O=K.pop();M.add((N,O))
					for P in(-1,0,1):
						for Q in(-1,0,1):
							if P==0 and Q==0:continue
							A,D=N+P,O+Q
							if G(A,D)and not E[A][D]and g[A][D]!=J:E[A][D]=I;K.append((A,D))
				L.append(M)
		return L
	def i():
		H=[[f]*C for A in range(B)];L=[]
		for A in range(B):
			for D in range(C):
				if H[A][D]or g[A][D]==J:continue
				M=g[A][D];K,N=[(A,D)],set();H[A][D]=I
				while K:
					O,P=K.pop();N.add((O,P))
					for(Q,R)in((-1,0),(1,0),(0,-1),(0,1)):
						E,F=O+Q,P+R
						if G(E,F)and not H[E][F]and g[E][F]==M:H[E][F]=I;K.append((E,F))
				L.append((M,N))
		return L
	U=h()
	if not U:return[A[:]for A in g]
	def j(cells):
		A={}
		for(C,D)in cells:B=g[C][D];A[B]=A.get(B,0)+1
		return max(A.values())-min(A.values())if A else-10**9
	D=max(U,key=j);V=[g[A][B]for(A,B)in D];W=min(set(V),key=V.count);X,Y=min(A for(A,B)in D),min(A for(B,A)in D);k={(A-X,B-Y)for(A,B)in D};K={(A-X,B-Y)for(A,B)in D if g[A][B]==W}
	if K:Z,a=min(A for(A,B)in K),min(A for(B,A)in K)
	else:Z=a=0
	def L(S):A=[A for(A,B)in S];B=[A for(B,A)in S];return min(A),min(B),max(A),max(B)
	def l(S):C,A,D,B=L(S);return B-A+1
	def m(S):A,B,C,C=L(S);return A,B
	def n(S):E,F,G,H=L(S);A,B,C,D=E-1,F-1,G+1,H+1;I={(A,B)for A in range(A,C+1)}|{(A,D)for A in range(A,C+1)};J={(A,B)for B in range(B,D+1)}|{(C,A)for A in range(B,D+1)};return I|J
	b=i();o=[B for(A,B)in b if A==W];c=[]
	for E in o:
		A=l(E);p,q=m(E);r=n(E);M={g[A][B]for(A,B)in r if G(A,B)};M.discard(0);s=next(iter(M))if M else 0;t,u=p-Z*A,q-a*A;F={(A+t,B+u)for(A,B)in k}
		if F:N=min(A for(A,B)in F);O=min(A for(B,A)in F)
		else:N=O=0
		H=set()
		for(v,w)in F:
			x,y=v-N,w-O;z,A0=N+x*A,O+y*A
			for A1 in range(A):
				for A2 in range(A):
					d,e=z+A1,A0+A2
					if G(d,e):H.add((d,e))
		c.append((s,H))
	P=[A[:]for A in g]
	for(Q,H)in c:
		for(R,S)in H:P[R][S]=Q
	for(Q,E)in b:
		for(R,S)in E:P[R][S]=Q
	return P