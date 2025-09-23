R=range
L=len
def p(a):
	C,B=L(a),L(a[0])
	def E(r,s):
		A=[0]*B
		for(E,C)in enumerate(r):
			D=E+s
			if C and 0<=D<B:A[D]=C
		return A
	for A in R(1,C+1):
		F=a[:A]
		for G in R(-B,B+1):
			H=True
			for D in R(C):
				if E(F[D%A],D//A*G)!=a[D]:H=False;break
			if H:return[E(F[B%A],B//A*G)for B in R(10)]
	return[a[A%C][:]for A in R(10)]
