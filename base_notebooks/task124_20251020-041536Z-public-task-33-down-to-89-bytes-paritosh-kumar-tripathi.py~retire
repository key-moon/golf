u=range
n=len
def p(s):
	D,B=n(s),n(s[0])
	def E(u,s):
		A=[0]*B
		for(E,C)in enumerate(u):
			D=E+s
			if C and 0<=D<B:A[D]=C
		return A
	for A in u(1,D+1):
		F=s[:A]
		for G in u(-B,B+1):
			H=True
			for C in u(D):
				if E(F[C%A],C//A*G)!=s[C]:H=False
			if H:return[E(F[B%A],B//A*G)for B in u(10)]