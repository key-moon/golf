def p(A):
	C={}
	for(D,H)in enumerate(A):
		for(E,F)in enumerate(H):
			if F:
				B=C.get(F)
				if B:B[0]=min(B[0],D);B[1]=max(B[1],D);B[2]=min(B[2],E);B[3]=max(B[3],E)
				else:C[F]=[D,D,E,E]
	G=min(C,key=lambda I:(C[I][1]-C[I][0]+1)*(C[I][3]-C[I][2]+1));B=C[G];return[[G]*(B[3]-B[2]+1)for A in range(B[1]-B[0]+1)]