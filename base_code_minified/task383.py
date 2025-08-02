def p(g):
	L,B=len(g),len(g[0]);C={}
	for M in g:
		for H in M:
			if H:C[H]=C.get(H,0)+1
	J=sorted(C,key=C.get);N,I=J[-1],J[-2]
	for D in range(L):
		for E in range(B):
			if g[D][E]==I:
				K=0
				for(F,G)in((1,0),(-1,0),(0,1),(0,-1)):
					try:
						if g[D+F][E+G]==I:K+=1
					except:pass
				if K-1:continue
				for(F,G)in((1,0),(-1,0),(0,1),(0,-1)):
					A=1
					while 1:
						try:B=g[D+F*A][E+G*A]
						except:break
						if B==N:A+=1
						elif B==0:g[D+F*A][E+G*A]=I;A+=1
						else:break
	return g