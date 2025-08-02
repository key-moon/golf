def p(A):
	F,G=len(A),len(A[0])
	for B in range(F):
		for C in range(G):
			H=A[B][C]
			if H:
				L=M=N=0
				for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
					if 0<=B+I<F and 0<=C+J<G and A[B+I][C+J]==H:L+=I;M+=J;N+=1
				if N==2:
					K=1
					while 1:
						K+=1;D,E=B+L*K,C+M*K
						if D<0 or D>=F or E<0 or E>=G:break
						if not A[D][E]:A[D][E]=H
	return A