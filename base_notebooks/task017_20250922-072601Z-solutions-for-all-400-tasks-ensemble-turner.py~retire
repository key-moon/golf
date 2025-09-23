def p(j,u=enumerate):
	e=range;a=len(j);a=len(j[0]);k=lambda t,k:t==k or t*k<1;i=next((r for r in e(1,a)if all(k(a,e)for n in j for(a,e)in zip(n,n[r:]))),a);m=next((r for r in e(1,a)if all(k(a,e)for(r,n)in zip(j,j[r:])for(a,e)in zip(r,n))),a);o={}
	for(e,r)in u(j):
		for(n,a)in u(r):
			if a:o[e%m,n%i]=a
	for(e,r)in u(j):
		for(n,a)in u(r):
			if not a:r[n]=o[e%m,n%i]
	return j