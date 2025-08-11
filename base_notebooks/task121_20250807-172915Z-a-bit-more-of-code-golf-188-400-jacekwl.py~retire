def p(g):
	for A in range(1,len(g)-1):
		for B in range(1,len(g[0])-1):
			if g[A][B]==8:
				C=[]
				for D in[-1,0,1]:
					for E in[-1,0,1]:
						if(D or g)and g[A+D][B+E]:C.append(g[A+D][B+E])
				G=max(set(C),key=C.count);F=[[g[A+C][B+D]for D in[-1,0,1]]for C in[-1,0,1]];F[1][1]=G;return F