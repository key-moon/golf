def p(j):
	for A in range(1,len(j)-1):
		for B in range(1,len(j[0])-1):
			if j[A][B]==8:
				C=[]
				for D in[-1,0,1]:
					for E in[-1,0,1]:
						if(D or j)and j[A+D][B+E]:C.append(j[A+D][B+E])
				G=max(set(C),key=C.count);F=[[j[A+C][B+D]for D in[-1,0,1]]for C in[-1,0,1]];F[1][1]=G;return F