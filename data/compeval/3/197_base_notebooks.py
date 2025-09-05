def	p(j):
	B=next((c	for	c	in	j	if	0	not	in	c),None)
	if	not	B:return	j
	c=[];[c.append(A)for	A	in	B	if	A	not	in	c]
	for(C,k)in	enumerate(j):
		if	0in	k	and	any(k):
			A=[];[A.append(c)for	c	in	k	if	c	not	in	A	and	c]
			if	len(c)==len(A):l=dict(zip(c,A));j[C]=[l[c]for	c	in	B]
	return	j