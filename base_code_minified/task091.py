def p(a):
	A=0,0,0,0;F,G=len(a),len(a[0])
	for D in range(G):
		for E in range(D+1,G):
			for B in range(F):
				if a[B][D]==a[B][E]!=0:
					C=1
					while B+C<F and a[B+C][D]==a[B+C][E]!=0:C+=1
					if C>A[0]:A=C,B,D,E
	return[B[A[2]:A[3]+1]for B in a[A[1]:A[1]+A[0]]]