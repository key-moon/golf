def	p(j):
	A=enumerate;c=next;F=lambda	k,W:k<1or	j[k-1][W]<1or	k>2and	j[k-1][W]==4and	j[k-2][W]>0;(k,B),(l,D),(a,l),l=[divmod(i,13)for(i,v)in	A(sum(j,[]))if	v==4];E=c(u	for	r	in	zip(*j)if	4	not	in	r	for	u	in	r	if	u);e=c(i	for(i,r)in	A(j)if	any(u==E	and	F(i,v)for(v,u)in	A(r)));G=c(i	for(i,r)in	A(zip(*j))if	any(u==E	and	F(v,i)for(v,u)in	A(r)))
	for	w	in	range(a-k-1):
		for	C	in	range(D-B-1):j[k+w+1][[D-C-1,B+C+1][j[k+1][B]==E]],j[e+w][G+C]=j[e+w][G+C],0
	return[r[B:D+1]for	r	in	j[k:a+1]]