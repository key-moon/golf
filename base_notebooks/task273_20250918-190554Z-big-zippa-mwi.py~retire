E=enumerate
R=range
def p(a):
	D=[A[:]for A in a];H=[[A for(A,B)in E(A)if B==4]for A in a]
	for(F,G)in E(H):
		for(I,A)in E(G):
			for B in G[I+1:]:
				for C in R(F+1,len(a)):
					if a[C][A]==4 and a[C][B]==4:
						for J in R(F+1,C):D[J][A+1:B]=[2]*(B-A-1)
	return D