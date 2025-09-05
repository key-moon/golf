def	p(j):
	def	u(A):
		c=[]
		for	B	in	A:
			if	B	not	in	c:c.append(B)
		return	c
	k=[u(c)for	c	in	j]
	if	all(k[0]==c	for	c	in	k):return[k[0]]
	return[[A]for	A	in	u([A	for	c	in	j	for	A	in	c])]