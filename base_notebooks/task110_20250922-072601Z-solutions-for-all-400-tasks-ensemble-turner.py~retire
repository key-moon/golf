def p(i,t=enumerate):
	b=range;l=len(i);l=len(i[0]);z=lambda r,l:r==l or r*l<1;g=next((r for r in b(1,l)if all(z(d,e)for l in i for(d,e)in zip(l,l[r:]))),l);a=next((r for r in b(1,l)if all(z(d,e)for(r,l)in zip(i,i[r:])for(d,e)in zip(r,l))),l);u={}
	for(e,r)in t(i):
		for(l,d)in t(r):
			if d:u[e%a,l%g]=d
	for(e,r)in t(i):
		for(l,d)in t(r):
			if not d:r[l]=u[e%a,l%g]
	return i