def p(a):
	o,d=len(a),len(a[0]);e=[(m,s)for m in(-4,0,4)for s in(-4,0,4)if m|s];t=range;q=[d]*10;r=[o]*10;j=[-1]*10;b=[-1]*10
	for s in t(o):
		for h in t(d):
			m=a[s][h]
			if h<q[m]:q[m]=h
			if s<r[m]:r[m]=s
			if h>j[m]:j[m]=h
			if s>b[m]:b[m]=s
	for m in t(1,10):
		if j[m]-q[m]==2 and b[m]-r[m]==2:c,i=q[m],r[m];break
	r=[[0]*d for m in a]
	for x in t(3):r[i+x][c:c+3]=a[i+x][c:c+3]
	z=[(s,m)for m in t(3)for s in t(3)if a[i+m][c+s]]
	for(f,u)in e:
		h=c+f;s=i+u;m=0
		for k in t(3):
			for y in t(3):
				v,l=h+y,s+k
				if 0<=v<d and 0<=l<o and a[l][v]:m=a[l][v];break
			if m:break
		if not m:continue
		h=c;s=i
		while 1:
			h+=f;s+=u
			if not(-3<h<d and-3<s<o):break
			for(y,k)in z:
				v,l=h+y,s+k
				if 0<=v<d and 0<=l<o:r[l][v]=m
	return r
