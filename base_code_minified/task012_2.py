def p(val_g):
	A=val_g;D=len(A);G=[[0]*D for A in A]
	for B in range(2,D-2):
		for C in range(2,D-2):
			E=A[B][C]
			if E and A[B-1][C]==A[B+1][C]==A[B][C-1]==A[B][C+1]!=E:
				J=A[B-1][C]
				for H in range(-2,3):
					for I in range(-2,3):
						F=abs(H)+abs(I)
						if F<3 or F==4:G[B+H][C+I]=E if F>2 else J
	return G