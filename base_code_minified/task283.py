def p(g):
	for(F,C)in enumerate(g):
		for(D,G)in enumerate(C):
			if G==5:
				E=0
				for(H,I)in((1,0),(-1,0),(0,1),(0,-1)):
					A,B=F+H,D+I
					if A<0 or B<0 or A>=len(g)or B>=len(g[0])or g[A][B]!=5:E+=1
				C[D]=(2,4,1)[E]
	return g