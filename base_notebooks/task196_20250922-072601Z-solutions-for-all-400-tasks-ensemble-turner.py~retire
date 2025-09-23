def p(j):
	m=range;s,e=len(j),len(j[0]);c=set();u=[n[:]for n in j]
	def p(l,u):
		if(l,u)in c or not(0<=l<s and 0<=u<e)or j[l][u]!=1:return[]
		c.add((l,u));return[(l,u)]+sum([p(l+n,u+m)for(n,m)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
	for D in m(s):
		for k in m(e):
			if j[D][k]==1 and(D,k)not in c:
				n=p(D,k);F,i,H,I=min(n[0]for n in n),max(n[0]for n in n),min(n[1]for n in n),max(n[1]for n in n)
				if len(n)==2*(i-F+I-H)and i>F and I>H and any(j[n][c]==0 for n in m(F+1,i)for c in m(H+1,I)):
					for(N,f)in n:u[N][f]=3
	return u