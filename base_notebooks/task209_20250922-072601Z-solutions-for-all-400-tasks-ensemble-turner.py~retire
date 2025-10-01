def p(g):
	S=None;from collections import Counter as k,deque as l;N,O=len(g),len(g[0]);P=[(A,B)for A in range(N)for B in range(O)if g[A][B]==4]
	if not P:return g
	q,r,s,t=min(A for(A,B)in P),max(A for(A,B)in P),min(A for(B,A)in P),max(A for(B,A)in P);A=[g[A][s:t+1][:]for A in range(q,r+1)];T=[[0 if g[A][B]==4 else g[A][B]for B in range(O)]for A in range(N)];m=k(B for A in T for B in A).most_common(1)[0][0];I=[[0]*O for A in range(N)];U=[]
	for B in range(N):
		for C in range(O):
			if I[B][C]or T[B][C]==m:continue
			b,L=[],l([(B,C)]);I[B][C]=1
			while L:
				E,F=L.popleft()
				if T[E][F]!=m:
					b.append((T[E][F],(E,F)))
					for V in[-1,0,1]:
						for W in[-1,0,1]:
							if V==0 and W==0:continue
							G,H=E+V,F+W
							if 0<=G<N and 0<=H<O and not I[G][H]:I[G][H]=1;L.append((G,H))
			if b:U.append(b)
	if not U:return A
	u=max(max(A for(B,(A,C))in A)for A in U);c=[A for A in U if max(A for(B,(A,C))in A)==u][0];v,w=min(A for(B,(A,C))in c),min(A for(B,(C,A))in c);M=[(A,(B-v,C-w))for(A,(B,C))in c];D=[[0 if A==4 else A for A in A]for A in A];X,Y=len(D),len(D[0])if D else 0
	if not D:return A
	d=k(B for A in D for B in A).most_common(1)[0][0];I=[[0]*Y for A in range(X)];J=[]
	for B in range(X):
		for C in range(Y):
			if I[B][C]or D[B][C]==d:continue
			n,L=D[B][C],l([(B,C)]);I[B][C]=1
			while L:
				E,F=L.popleft()
				if D[E][F]==n and D[E][F]!=d:
					J.append((D[E][F],(E,F)))
					for(V,W)in[(1,0),(-1,0),(0,1),(0,-1)]:
						G,H=E+V,F+W
						if 0<=G<X and 0<=H<Y and not I[G][H]and D[G][H]==n:I[G][H]=1;L.append((G,H))
	if not J:return A
	e=max(A for(B,(C,A))in M)-min(A for(B,(C,A))in M)+1 if M else 1;f=max(A for(B,(A,C))in M)-min(A for(B,(A,C))in M)+1 if M else 1;x=max(A for(B,(C,A))in J)-min(A for(B,(C,A))in J)+1 if J else 1;y=max(A for(B,(A,C))in J)-min(A for(B,(A,C))in J)+1 if J else 1;Z=max(1,(x+e-1)//e if e else 1,(y+f-1)//f if f else 1);o=[Z,Z+1]
	if Z>1:o.append(Z-1)
	h,i=S,S
	for a in o:
		Q=[(A,(B*a+D,C*a+E))for(A,(B,C))in M for D in range(a)for E in range(a)];z=max(A for(B,(A,C))in Q)+1 if Q else 0;A0=max(A for(B,(C,A))in Q)+1 if Q else 0
		for A1 in range(max(0,len(A)-z+1)):
			for A2 in range(max(0,len(A[0])-A0+1)):
				p=[(A,(B+A1,C+A2))for(A,(B,C))in Q];K={(B,C):D for(D,(B,C))in p if 0<=B<len(A)and 0<=C<len(A[0])}
				if not K or any(A[B][C]==4 for(B,C)in K):continue
				R={(A,B):D[A][B]for A in range(X)for B in range(Y)if D[A][B]!=d}
				if R:A3=sum(1 for((A,B),C)in R.items()if K.get((A,B))==C);A4=sum(1 for((A,B),C)in R.items()if K.get((A,B))is not S and K.get((A,B))!=C);A5=sum(1 for((A,B),C)in R.items()if K.get((A,B))is S);A6=sum(1 for A in K if A not in R);j=A3*200-A4*500-A5*1000-A6
				else:j=-len(K)
				if h is S or j>h:h,i=j,p
	if i:
		for(A7,(B,C))in i:
			if 0<=B<len(A)and 0<=C<len(A[0]):A[B][C]=A7
	return A