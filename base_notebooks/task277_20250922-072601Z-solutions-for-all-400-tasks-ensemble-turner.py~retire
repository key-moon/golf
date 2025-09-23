def p(j):
	s,s=len(j),len(j[0]);p=[[0]*s for r in j];o=[]
	for r in range(s):
		for t in range(s):
			if j[r][t]==8 and not p[r][t]:
				v=[(r,t)];p[r][t]=1;l=[]
				while v:
					r,t=v.pop();l.append((r,t))
					for a in(-1,0,1):
						for k in(-1,0,1):
							if a==k==0:continue
							b,x=r+a,t+k
							if 0<=b<s and 0<=x<s and not p[b][x]and j[b][x]==8:p[b][x]=1;v.append((b,x))
				o.append(l)
	if not o:return[r[:]for r in j]
	def d(b):r=min(r for(r,t)in b);t=min(r for(t,r)in b);return tuple(sorted((b-r,x-t)for(b,x)in b))
	i={}
	for r in o:i.setdefault(d(r),[]).append(r)
	c=min(len(r)for r in i.values());l=[t for(b,r)in i.items()if len(r)==c for t in r]
	def t(b):return min(r for(r,t)in b),min(r for(t,r)in b)
	c=min(l,key=t);i=[r[:]for r in j]
	for r in range(s):
		for t in range(s):
			if i[r][t]==8:i[r][t]=1
	for(r,t)in c:i[r][t]=2
	return i