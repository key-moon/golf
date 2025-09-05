def	f(j,A,c,E):
	if	not(0<=A<len(j)and	0<=c<len(j[0])):return
	if	j[A][c]:return
	j[A][c]=E
	for(k,B)in[(0,-1),(0,1),(-1,0),(1,0)]:f(j,A+k,c+B,E)
def	p(j):
	l,A=len(j),len(j[0]);f(j,0,0,1)
	for	a	in	range(4):f(j,l//2-1+a%2,A//2-1+a//2,2)
	f(j,l-1,A-1,3);return	j