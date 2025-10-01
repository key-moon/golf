def p(g):
	O=None
	if not g or not g[0]:return[list(A)for A in g]
	E=tuple(tuple(A)for A in g);f,h=len(E),len(E[0])
	def J(idxs):A=[A for(A,B)in idxs];B=[A for(B,A)in idxs];return min(A),min(B),max(A),max(B)
	def P(idxs):
		A=idxs
		if not A:return set()
		B,C,D,D=J(A);return{(A-B,D-C)for(A,D)in A}
	K=tuple(tuple(reversed(A))for A in E);from collections import Counter as i;F=i(B for A in K for B in A);Q=max(F.items(),key=lambda kv:kv[1])[0];A={}
	for R in range(f):
		B=K[R]
		for S in range(h):
			T=B[S]
			if T!=Q:A.setdefault(T,set()).add((R,S))
	if not A:return[list(A)for A in E]
	C=max(A,key=lambda c:len(A[c]));G=P(A[C]);D=O
	for(F,H)in A.items():
		if F==C:continue
		if len(H)==len(A[C]):continue
		j=P(H);I={(2*A+C,2*B+D)for(A,B)in j for C in(0,1)for D in(0,1)}
		if I and G:
			U=[A for(A,B)in I];V=[A for(B,A)in I];W=[A for(A,B)in G];X=[A for(B,A)in G];k=min(W)-max(U);l=max(W)-min(U);m=min(X)-max(V);n=max(X)-min(V);o=I;p=G;L=0
			for q in range(k,l+1):
				for r in range(m,n+1):
					Y=sum(1 for(A,B)in o if(A+q,B+r)in p)
					if Y>L:L=Y
			Z=L
		else:Z=0
		a,a,a,s=J(H);b=len(H);t=Z-2*b;c=t,b,s,F
		if D is O or c>D:D=c
	if D is O:d=[A for A in A if A!=C];M=max(d,key=lambda c:len(A[c]))if d else C
	else:M=D[3]
	u,v,w,x=J(A[M]);N=[list(K[A][v:x+1])for A in range(u,w+1)]
	for y in range(len(N)):
		B=N[y]
		for e in range(len(B)):
			if B[e]!=M:B[e]=Q
	z=tuple(tuple(reversed(A))for A in N);return[list(A)for A in z]
