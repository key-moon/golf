def p(g):
	o=False;O=True;from collections import Counter as p,deque;K,L=len(g),len(g[0]);P=[[o]*L for A in range(K)];R=[]
	for A in range(K):
		for B in range(L):
			if g[A][B]==0 and not P[A][B]:
				S=deque([(A,B)]);P[A][B]=O;D=[];Z=A==0 or B==0 or A==K-1 or B==L-1
				while S:
					a,b=S.popleft();D.append((a,b))
					for(q,r)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=a+q,b+r
						if 0<=E<K and 0<=F<L and not P[E][F]and g[E][F]==0:
							P[E][F]=O
							if E==0 or F==0 or E==K-1 or F==L-1:Z=O
							S.append((E,F))
				if not Z:R.append(D)
	if not R:return[A[:]for A in g]
	D=max(R,key=len);s=min(A for(A,B)in D);t=min(A for(B,A)in D);u=max(A for(A,B)in D);v=max(A for(B,A)in D);w,x=max(0,s-1),max(0,t-1);y,z=min(K-1,u+1),min(L-1,v+1);G=[A[x:z+1]for A in g[w:y+1]];c,d=len(G),len(G[0]);e=p(B for A in G for B in A);A0=max(e,key=e.get);f,T,U,h=set(),None,-1,-1;A1={A for B in G for A in B if A!=A0}
	for i in A1:
		C=[(A,B)for A in range(c)for B in range(d)if G[A][B]==i]
		if not C:continue
		M={}
		for(A,B)in C:
			if B in M:
				H,I=M[B]
				if A<H:H=A
				if A>I:I=A
				M[B]=H,I
			else:M[B]=A,A
		A2={(D,A)for(A,(B,C))in M.items()for D in range(B,C+1)};N={}
		for(A,B)in C:
			if A in N:
				H,I=N[A]
				if B<H:H=B
				if B>I:I=B
				N[A]=H,I
			else:N[A]=B,B
		A3={(A,D)for(A,(B,C))in N.items()for D in range(B,C+1)};A4=min(A for(A,B)in C);A5=max(A for(A,B)in C);j={B for(A,B)in C if A==A4};k={B for(A,B)in C if A==A5};A6=j if len(j)>=len(k)else k;V={(B,A)for(B,A)in A2 if A in A6};A7=min(A for(B,A)in C);A8=max(A for(B,A)in C);l={A for(A,B)in C if B==A7};m={A for(A,B)in C if B==A8};A9=m if len(m)>=len(l)else l;Q={(A,B)for(A,B)in A3 if A in A9};W=o
		if len(V)>len(Q):J=V
		elif len(Q)>len(V):J=Q;W=O
		else:J=Q;W=O
		if W:
			AA=set(C);X={}
			for(A,_)in C:X[A]=X.get(A,0)+1
			AB={A for(A,B)in C}
			if len(AB)<=2:J={A for A in J if not(A not in AA and X.get(A[0],0)==2)}
		Y=len(J)-len(C);n=len(J)
		if Y>U or Y==U and n>h:U,h,T,f=Y,n,i,J
	if T is not None:
		for(A,B)in f:
			if 0<=A<c and 0<=B<d:G[A][B]=T
	return G