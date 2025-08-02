def p(A):
	for C in A:
		D=None;B=0
		while B<len(C):
			if C[B]==2:
				if D:
					for E in range(D+1,B):C[E]=9
				while B+1<len(C)and C[B+1]==2:B+=1
				D=B
			B+=1
	return A