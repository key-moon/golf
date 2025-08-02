def p(A):
	D=len(A);J=[(0,1),(1,0),(0,-1),(-1,0)];E=F=G=0
	while 1:
		A[F][G]=3;H,I=J[E];B,C=F+H,G+I
		if B<0 or B>=D or C<0 or C>=D or A[B][C]:
			E=(E+1)%4;H,I=J[E];B,C=F+H,G+I
			if B<0 or B>=D or C<0 or C>=D or A[B][C]:break
		F,G=B,C
	return A