def p(e,t=range,E=enumerate):
	F={}
	for(A,B)in E(e):
		for(C,D)in E(B):
			if D:F.setdefault(D,[]).append((A,C))
	for D in F:
		(A,C),(B,E)=F[D];H,E=(B>A)-(B<A),(E>C)-(E<C)
		for G in t(abs(B-A)+1):e[A+G*H][C+G*E]=D
	return e