def	p(j,A=range):
	c,B=len(j),len(j[0]);k=[[0]*B	for	c	in	A(c)];E=[]
	for	l	in	A(c):
		for	C	in	A(B):
			if	l*C==0	or	l==c-1or	C==B-1:
				if	j[l][C]==0:k[l][C]=1;E.append((l,C))
	while	E:
		a,F=E.pop(0)
		for(e,G)in[(-1,0),(1,0),(0,-1),(0,1)]:
			w,D=a+e,F+G
			if	0<=w<c	and	0<=D<B	and	j[w][D]==0and	not	k[w][D]:k[w][D]=1;E.append((w,D))
	b=[[j[c][A]if	j[c][A]!=0	or	k[c][A]else	1for	A	in	A(B)]for	c	in	A(c)];return	b