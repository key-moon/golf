def p(j):
	A=[K[:]for K in j];c,E=len(j),len(j[0]);k=set();r=[]
	for l in range(c):
		for J in range(E):
			if j[l][J]!=2 and(l,J)not in k:
				a,t=[],[(l,J)];k.add((l,J));e=0
				while t:
					K,w=t.pop();a.append((K,w))
					if j[K][w]==0:e+=1
					for(L,s)in[(0,1),(1,0),(0,-1),(-1,0)]:
						if 0<=K+L<c and 0<=w+s<E and j[K+L][w+s]!=2 and(K+L,w+s)not in k:k.add((K+L,w+s));t.append((K+L,w+s))
				r.append((e,a))
	d=max(K[0]for K in r);f=min(K[0]for K in r)
	for(e,a)in r:
		k=1 if e==d else 8 if e==f else 0
		if k:
			for(K,w)in a:
				if j[K][w]==0:A[K][w]=k
	return A