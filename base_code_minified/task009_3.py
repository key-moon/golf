def p(A):
	E=len(A)//3+1;F=len(A[0])//3+1;G=[[0]*F for A in range(E)]
	for C in range(E):
		for D in range(F):
			for H in(0,1):
				for I in(0,1):
					B=A[3*C+H][3*D+I]
					if B:G[C][D]=B
	for C in range(E):
		for D in range(F):
			B=G[C][D]
			if B:
				for J in range(F):
					if B:G[C][J]=B
				for J in range(E):
					if B:G[J][D]=B
	for C in range(E):
		for D in range(F):
			B=G[C][D]
			if B:
				for H in(0,1):
					for I in(0,1):A[3*C+H][3*D+I]=B
	return A