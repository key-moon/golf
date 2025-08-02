def p(A):
	G=len(A)
	for(E,B)in enumerate(A):
		if 8 in B:J=B.index(8);break
	for(F,B)in enumerate(A):
		if F==E:continue
		H=abs(E-F);I=1 if F<E else-1;C=J+I*H
		if H&1:
			D=C-I
			if 0<=D<G:B[D]=5
		else:
			for D in range(C-2,C+1)if F<E else range(C,C+3):
				if 0<=D<G:B[D]=5
	return A