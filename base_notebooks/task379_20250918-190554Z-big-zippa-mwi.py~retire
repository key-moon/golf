def p(a):
	J=None;F=range;K=lambda g:[list(A)for A in zip(*g)];B=a;L=0
	if not any(all(A==8 for A in A)for A in a):B,L=K(a),1
	H,M=len(B),len(B[0]);G=[A[:]for A in B];N=[A for A in F(H)if all(A==8 for A in B[A])]
	for D in F(H):
		for C in F(M):
			if B[D][C]!=2:continue
			for A in(max([A for A in N if A<D],default=J),min([A for A in N if A>D],default=J)):
				if A is J:continue
				for E in(A-1,A,A+1):
					if 0<=E<H:
						for I in(C-1,C,C+1):
							if 0<=I<M:G[E][I]=2 if E==A and I==C else 8
				O=1-2*(A<D)
				for E in F(D,A-O,O):G[E][C]=2
	return K(G)if L else G