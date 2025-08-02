def p(A):
	M,C=len(A),len(A[0]);D={}
	for N in A:
		for I in N:
			if I:D[I]=D.get(I,0)+1
	K=sorted(D,key=D.get);O,J=K[-1],K[-2]
	for E in range(M):
		for F in range(C):
			if A[E][F]==J:
				L=0
				for(G,H)in((1,0),(-1,0),(0,1),(0,-1)):
					try:
						if A[E+G][F+H]==J:L+=1
					except:pass
				if L-1:continue
				for(G,H)in((1,0),(-1,0),(0,1),(0,-1)):
					B=1
					while 1:
						try:C=A[E+G*B][F+H*B]
						except:break
						if C==O:B+=1
						elif C==0:A[E+G*B][F+H*B]=J;B+=1
						else:break
	return A