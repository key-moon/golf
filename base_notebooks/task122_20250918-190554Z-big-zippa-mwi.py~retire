def p(g,L=len,R=range):
	for A in R(L(g)):
		for D in R(L(g[0])):
			if g[A][D]==2:
				if g[A+1].count(3)>1:
					for B in R(3):
						for C in R(3):
							g[A+B][D+C+2]=g[A+B][D+C]
							if g[A+B][D+C]==2 and C<2:g[A+B][D+C]=0
					return g
				else:
					for B in R(3):
						for C in R(3):
							g[A+B+2][D+C]=g[A+B][D+C]
							if g[A+B][D+C]==2 and B<2:g[A+B][D+C]=0
					return g