def p(A):
	H,D=len(A),len(A[0]);E=[[0]*D for A in A]
	for(I,J)in enumerate(A):
		for(K,L)in enumerate(J):
			if L==5:
				for B in(-1,0,1):
					for C in(-1,0,1):
						F=I+B
						if 0<=F<H:
							G=K+C
							if 0<=G<D:E[F][G]=5 if B and C else 1 if B or C else 0
	return E