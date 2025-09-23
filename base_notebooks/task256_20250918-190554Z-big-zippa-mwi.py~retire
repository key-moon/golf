def p(j,A=range):
	E=len(j)
	for B in A(E):
		if j[B][0]==2:
			C=0
			while C<E and j[B][C]==2:C+=1
			for D in A(E):
				for F in A((C+B-D)*(D!=B)):j[D][F]=3-2*(D>B)
	return j