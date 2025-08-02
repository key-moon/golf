def p(g):
	for B in g:
		C=None;A=0
		while A<len(B):
			if B[A]==2:
				if C:
					for D in range(C+1,A):B[D]=9
				while A+1<len(B)and B[A+1]==2:A+=1
				C=A
			A+=1
	return g