def p(s):
	A,A=len(s),len(s[0]);D=[[0]*A for B in range(A)];C={};[[C.setdefault(s[B][A],[]).append((B,A))for A in range(A)if s[B][A]]for B in range(A)]
	for(s,B)in C.items():
		F,G=B[len(B)//2];E=abs(B[1][0]-B[0][0])or abs(B[1][1]-B[0][1])if len(B)>1 else 0
		if E<=0:break
		for B in range(1,max(F,A-1-F,G,A-1-G)//E+1):C,H,I,J=F-B*E,F+B*E,G-B*E,G+B*E;0<=C<A and[D[C].__setitem__(A,s)for A in range(max(0,I),min(A,J+1))];0<=H<A and[D[H].__setitem__(A,s)for A in range(max(0,I),min(A,J+1))];0<=I<A and[D[A].__setitem__(I,s)for A in range(max(0,C),min(A,H+1))];0<=J<A and[D[A].__setitem__(J,s)for A in range(max(0,C),min(A,H+1))]
		D[F][G]=s
	return D