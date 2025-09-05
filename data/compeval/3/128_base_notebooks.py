def	p(j):
	E=[[0]*len(j[0])for	a	in	j];c=set()
	for	B	in	range(len(j)):
		for	k	in	range(len(j[0])):
			if	j[B][k]and(B,k)not	in	c:
				D,l=[(B,k)],[(B,k)];c.add((B,k));F=j[B][k]
				while	l:
					a,A=l.pop()
					for(e,C)in[(0,1),(1,0),(0,-1),(-1,0)]:
						if	0<=a+e<len(j)and	0<=A+C<len(j[0])and	j[a+e][A+C]==F	and(a+e,A+C)not	in	c:c.add((a+e,A+C));D.append((a+e,A+C));l.append((a+e,A+C))
				w=max(a	for(a,A)in	D)-min(a	for(a,A)in	D)+1
				for(a,A)in	D:E[a-w][A]=F
	return	E