def p(j,A=enumerate):
	c=[]
	for(E,k)in A(j):
		for(W,l)in A(k):
			if l not in[0,8]:c+=[[E,W,l]];j[E][W]=0
	J=c[0][:];c=[[c[0]-J[0],c[1]-J[1],c[2]]for c in c]
	for(E,k)in A(j):
		for(W,l)in A(k):
			if l==8:
				j[E][W]=J[2]
				for a in c:j[E+a[0]][W+a[1]]=a[2]
	return j