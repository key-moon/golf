def p(g):
	C=len(g);I=[(0,1),(1,0),(0,-1),(-1,0)];D=E=F=0
	while 1:
		g[E][F]=3;G,H=I[D];A,B=E+G,F+H
		if A<0 or A>=C or B<0 or B>=C or g[A][B]:
			D=(D+1)%4;G,H=I[D];A,B=E+G,F+H
			if A<0 or A>=C or B<0 or B>=C or g[A][B]:break
		E,F=A,B
	return g