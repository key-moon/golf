def p(p):
	t=range;p=[m[:]for m in p];g,F=len(p),len(p[0]);n={}
	for m in t(g):
		for i in t(F):
			if p[m][i]:n[p[m][i]]=n.get(p[m][i],0)+1
	m,i,a=next((m,i,p[m][i])for m in t(g)for i in t(F)if p[m][i]and n[p[m][i]]==1)
	for(G,r)in[(0,1),(1,0),(0,-1),(-1,0)]:
		d,K=m+G,i+r
		if(d<0)|(d>=g)|(K<0)|(K>=F)|(p[d][K]==0):
			e=1
			while(0<=m-e*G<g)&(0<=i-e*r<F):
				if p[m-e*G][i-e*r]==0:p[m-e*G][i-e*r]=a
				e+=1
	return p