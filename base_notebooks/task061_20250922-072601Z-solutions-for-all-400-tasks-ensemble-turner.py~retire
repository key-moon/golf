def p(t,z=enumerate):
	f=range;e=len(t);e=len(t[0]);k=lambda i,f:i==f or i*f<1;g=next((i for i in f(1,e)if all(k(d,e)for f in t for(d,e)in zip(f,f[i:]))),e);a=next((i for i in f(1,e)if all(k(d,e)for(i,f)in zip(t,t[i:])for(d,e)in zip(i,f))),e);C={}
	for(e,i)in z(t):
		for(f,d)in z(i):
			if d:C[e%a,f%g]=d
	for(e,i)in z(t):
		for(f,d)in z(i):
			if not d:i[f]=C[e%a,f%g]
	return t