def p(A):
	C=len(A)
	for D in range(C):
		for E in range(C):
			if A[D][E]==2:
				K=[(B,F)for(B,F)in((1,0),(-1,0),(0,1),(0,-1))if 0<=D+B<C and 0<=E+F<C and A[D+B][E+F]>2];B,F=K;J=-B[0]-F[0],-B[1]-F[1];L=A[D+B[0]][E+B[1]];G=0
				while 1:
					for(M,N)in(B,F,(B[0]+F[0],B[1]+F[1])):
						H=D+M+G*J[0];I=E+N+G*J[1]
						if H<0 or H>=C or I<0 or I>=C:return A
						A[H][I]=L
					G+=1