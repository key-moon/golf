def	p(j):
	B=range;c,C=len(j),len(j[0]);k=[]
	for	A	in	B(c):
		if	A==0	or	j[A]!=j[A-1]:k.append([j[A][0]])
	l=[];D=-1
	for	a	in	B(C):
		if	a==0	or	any(j[A][a]!=j[A][a-1]for	A	in	B(c)):l.append(j[0][a])
	if	len(k)>1:return	k
	else:return[l]