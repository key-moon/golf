def p(g):
	E,F=len(g),len(g[0])
	for A in range(E):
		for B in range(F):
			G=g[A][B]
			if G:
				K=L=M=0
				for(H,I)in((1,0),(-1,0),(0,1),(0,-1)):
					if 0<=A+H<E and 0<=B+I<F and g[A+H][B+I]==G:K+=H;L+=I;M+=1
				if M==2:
					J=1
					while 1:
						J+=1;C,D=A+K*J,B+L*J
						if C<0 or C>=E or D<0 or D>=F:break
						if not g[C][D]:g[C][D]=G
	return g