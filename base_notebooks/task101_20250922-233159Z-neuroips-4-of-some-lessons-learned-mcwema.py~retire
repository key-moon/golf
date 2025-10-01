from collections import Counter,deque
def p(I):
	if not I or not I[0]:return[]
	T={};[T.__setitem__(A,T.get(A,0)+1)for B in I for A in B];l=max(T,key=T.get);D,E=len(I),len(I[0]);U=[[0]*E for A in range(D)];V=[];q=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for F in range(D):
		for G in range(E):
			if U[F][G]or I[F][G]==l:continue
			X=deque([(F,G)]);U[F][G]=1;m=[]
			while X:Y,Z=X.popleft();m.append((I[Y][Z],(Y,Z)));[X.append((A,B))or U[A].__setitem__(B,1)for(C,F)in q for(A,B)in[(Y+C,Z+F)]if 0<=A<D and 0<=B<E and not U[A][B]and I[A][B]!=l]
			V.append(m)
	if not V:return I
	V.sort(key=lambda c:len({A for(A,B)in c}),reverse=1);n=V[0];a=lambda pxs:set()if not pxs else{(A,(B-min(A for(B,(A,C))in pxs),C-min(A for(B,(C,A))in pxs)))for(A,(B,C))in pxs};r=Counter(A for(A,B)in n);o=max(r.items(),key=lambda kv:(kv[1],-kv[0]))[0];b=[]
	for W in(1,2,3):
		c={(A,(B*W+D,C*W+E))for(A,(B,C))in a(n)for D in range(W)for E in range(W)};d={(A,B)for(A,B)in c if A!=o};M=set();H=set()
		if d:
			H={(A,B)for(C,(A,B))in d};N,O=[A for(A,B)in H],[A for(B,A)in H];A,B,J,K=min(N)-1,min(O)-1,max(N)+1,max(O)+1;e={(A,B)for A in range(A,J+1)}|{(A,K)for A in range(A,J+1)}|{(A,B)for B in range(B,K+1)}|{(J,A)for A in range(B,K+1)};f=d|{(0,A)for A in e};L=a(f);g,h=[A for(B,(A,C))in L],[A for(B,(C,A))in L];i,j=max(g)+1,max(h)+1
			for A in range(-i+1,D):
				for B in range(-j+1,E):
					C=1;P=0
					for(Q,(F,G))in L:
						R,S=A+F,B+G
						if 0<=R<D and 0<=S<E:P=1;C=C and I[R][S]==Q
						else:C=C and Q==0
					if C and P:M.add((A,B))
		if not M:
			k={(A,B)for(A,B)in c if A==o}
			if not k:continue
			H={(A,B)for(C,(A,B))in k};N,O=[A for(A,B)in H],[A for(B,A)in H];A,B,J,K=min(N)-1,min(O)-1,max(N)+1,max(O)+1;e={(A,B)for A in range(A,J+1)}|{(A,K)for A in range(A,J+1)}|{(A,B)for B in range(B,K+1)}|{(J,A)for A in range(B,K+1)};f=k|{(0,A)for A in e};L=a(f);g,h=[A for(B,(A,C))in L],[A for(B,(C,A))in L];i,j=max(g)+1,max(h)+1
			for A in range(-i+1,D):
				for B in range(-j+1,E):
					C=1;P=0
					for(Q,(F,G))in L:
						R,S=A+F,B+G
						if 0<=R<D and 0<=S<E:P=1;C=C and I[R][S]==Q
						else:C=C and Q==0
					if C and P:M.add((A,B))
		if not M:continue
		s,t=min(A for(A,B)in H),min(A for(B,A)in H)
		for(u,v)in M:w,x=u-s+1,v-t+1;b.append({(A,(B+w,C+x))for(A,(B,C))in c})
	p=[list(A)for A in I];[p[A].__setitem__(B,C)for(C,(A,B))in set().union(*b)if 0<=A<D and 0<=B<E];return p
