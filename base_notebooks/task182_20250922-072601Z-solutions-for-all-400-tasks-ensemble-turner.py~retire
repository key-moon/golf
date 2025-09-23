def p(g):
	h=False;from collections import Counter as q,deque;o,t=len(g),len(g[0]);x=q(B for s in g for B in s).most_common(1)[0][0]
	def T(j,r):
		m=g[j][r];y=deque([(j,r)]);n={(j,r)};z=[(j,r)]
		while y:
			l,e=y.popleft()
			for(i,h)in((1,0),(-1,0),(0,1),(0,-1)):
				s,B=l+i,e+h
				if 0<=s<o and 0<=B<t and(s,B)not in n and g[s][B]==m:n.add((s,B));y.append((s,B));z.append((s,B))
		return m,z
	d=[[h]*t for s in range(o)];z=[]
	for B in range(o):
		for y in range(t):
			if g[B][y]!=x and not d[B][y]:
				n,s=T(B,y)
				for(j,l)in s:d[j][l]=True
				z.append((n,s))
	def l(r):s=r;B=[s for(s,B)in s];y=[s for(B,s)in s];return min(B),min(y),max(B),max(y)
	def W(r):
		y=r;m,n,o,t=l(y);z=set(y)
		for s in range(m,o+1):
			for B in range(n,t+1):
				e=s in(m,o)or B in(n,t)
				if e and(s,B)not in z:return h
				if not e and(s,B)in z:return h
		return True
	e=None
	for(n,s)in z:
		if n==5 and W(s):e=s;break
	if e is None:return[list(s)for s in g]
	i,h,P,o=l(e);c,f,e,a=i+1,h+1,P-1,o-1;b=[(s,B)for s in range(c,e+1)for B in range(f,a+1)];m=[(s,B)for(s,B)in b if g[s][B]!=0]
	if not m:return[list(s)for s in g]
	h=min(s for(s,B)in m);e=min(s for(B,s)in m);e={(s-h,B-e)for(s,B)in m};j=q(g[s][B]for(s,B)in m).most_common(1)[0][0];g=[s[:]for s in g]
	for(n,s)in z:
		i,h,P,o=l(s);o={(s-i,B-h)for(s,B)in s}
		if o==e:
			for(B,y)in s:g[B][y]=j
	return g