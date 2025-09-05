def	p(j,A=range,c=enumerate):
	E=len(j);k=len(j[0]);C=[[0]*k	for	_	in	A(E)];l={v	for	A	in	j	for	v	in	A	if	v}
	for	B	in	l:
		a=[b	for(b,A)in	c(j)for	v	in	A	if	v==B];D=[d	for(b,A)in	c(j)for(d,v)in	c(A)if	v==B];e,F=min(a),max(a)+1;w,G=min(D),max(D)+1
		for	b	in	A(e,F):
			for	d	in	A(w,G):C[b][d]=B
	return	C