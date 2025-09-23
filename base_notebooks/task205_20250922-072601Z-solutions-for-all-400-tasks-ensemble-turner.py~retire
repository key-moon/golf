def p(g):
	if not g or not g[0]:return[]
	f,T=len(g),len(g[0]);M=set();e=[]
	for C in range(f):
		for z in range(T):
			if(C,z)in M:continue
			u=g[C][z];O=[(C,z)];p=[];M.add((C,z))
			while O:
				U,d=O.pop();p.append((U,d))
				for(Y,Z)in((1,0),(-1,0),(0,1),(0,-1)):
					n,J=U+Y,d+Z
					if 0<=n<f and 0<=J<T and(n,J)not in M and g[n][J]==u:M.add((n,J));O.append((n,J))
			if len(p)>len(e):e=p
	s=min(t for(t,e)in e);b=max(t for(t,e)in e);c=min(t for(e,t)in e);x=max(t for(e,t)in e);g=[t[c:x+1]for t in g[s:b+1]]
	if not g:return[]
	m=[t[:]for t in g];o=[e for t in m for e in t];H=max(set(o),key=o.count);t=[t[:]for t in m];K,L=len(t),len(t[0])
	while t and sum(1 for t in t[0]if t==H)*2<=L:t.pop(0);K-=1
	while t and sum(1 for t in t[-1]if t==H)*2<=L:t.pop();K-=1
	if not t:return[]
	e=list(zip(*t))
	while e and sum(1 for t in e[0]if t==H)*2<=len(t):e.pop(0)
	while e and sum(1 for t in e[-1]if t==H)*2<=len(t):e.pop()
	if not e:return[]
	m=[list(t)for t in zip(*e)];o=[e for t in m for e in t];H=max(set(o),key=o.count);g=min(set(o),key=o.count);K,L=len(m),len(m[0]);N=[[H]*L for t in range(K)];R=[(t,C)for(t,e)in enumerate(m)for(C,m)in enumerate(e)if m==g]
	if not R:return N
	t={t for(t,e)in R};e={t for(e,t)in R}
	for C in t:N[C]=[g]*L
	for z in e:
		for C in range(K):N[C][z]=g
	return N