def p(A):
	H=0,4,8
	for J in range(3):
		for K in range(3):
			B,C=H[J],H[K];E=None;I=set()
			for D in range(B,B+3):
				for F in range(C,C+3):
					G=A[D][F]
					if G and G!=5:E=G;I.add(D)
			if E and len(I)>1:
				for D in range(B,B+3):
					for F in range(C,C+3):A[D][F]=E
	return A