def p(q):
	r,z=len(q),len(q[0]);d,r,f,G=r,z,-1,-1
	for y in range(r):
		for o in range(z):
			if q[y][o]!=0:
				if y<d:d=y
				if y>f:f=y
				if o<r:r=o
				if o>G:G=o
	if f<0:return[[]]
	N=[tuple(q[y][r:G+1])for y in range(d,f+1)];H=[];z=None
	for o in N:
		if o!=z:H.append(o);z=o
	p=list(zip(*H))if H else[];J=[];z=None
	for o in p:
		if o!=z:J.append(o);z=o
	return[list(y)for y in zip(*J)]