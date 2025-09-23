def p(a):
	e,e=len(a),len(a[0]);m=[[0]*e for n in range(e)];g={};[[g.setdefault(a[n][l],[]).append((n,l))for l in range(e)if a[n][l]]for n in range(e)]
	for(a,n)in g.items():
		n.sort();i,r=n[len(n)//2];l=abs(n[1][0]-n[0][0])or abs(n[1][1]-n[0][1])if len(n)>1 else 0
		if l<=0:
			for p in range(len(n)):
				for r in range(p+1,len(n)):
					if(y:=max(abs(n[p][0]-n[r][0]),abs(n[p][1]-n[r][1]))):l=y;break
				if l:break
		l=l or 1
		for I in range(1,max(i,e-1-i,r,e-1-r)//l+1):z,s,t,u=i-I*l,i+I*l,r-I*l,r+I*l;0<=z<e and[m[z].__setitem__(n,a)for n in range(max(0,t),min(e,u+1))];0<=s<e and[m[s].__setitem__(n,a)for n in range(max(0,t),min(e,u+1))];0<=t<e and[m[n].__setitem__(t,a)for n in range(max(0,z),min(e,s+1))];0<=u<e and[m[n].__setitem__(u,a)for n in range(max(0,z),min(e,s+1))]
		m[i][r]=a
	return m