def p(g):
	F,G=len(g),len(g[0]);Q=[o[:]for o in g];E=[[False]*G for o in range(F)];S=[(1,0),(-1,0),(0,1),(0,-1)]
	for d in range(F):
		for s in range(G):
			if E[d][s]:continue
			T=g[d][s];p=[(d,s)];E[d][s]=True;i=[(d,s)];a=f=d;b=z=s
			while p:
				s,r=p.pop()
				for(t,V)in S:
					o,B=s+t,r+V
					if 0<=o<F and 0<=B<G and not E[o][B]and g[o][B]==T:
						E[o][B]=True;p.append((o,B));i.append((o,B))
						if o<a:a=o
						if o>f:f=o
						if B<b:b=B
						if B>z:z=B
			P=f-a+1;R=z-b+1
			if P==R and len(i)==P*R:
				W=2 if P%2==0 else 7
				for(s,r)in i:Q[s][r]=W
	return Q