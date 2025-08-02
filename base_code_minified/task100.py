def p(A):
	C={}
	for(D,G)in enumerate(A):
		for(E,F)in enumerate(G):
			if F:B=C.setdefault(F,[D,D,E,E]);B[0]=min(B[0],D);B[1]=max(B[1],D);B[2]=min(B[2],E);B[3]=max(B[3],E)
	H=max(C,key=lambda F:(C[F][1]-C[F][0]+1)*(C[F][3]-C[F][2]+1));return[[H]*2]*2