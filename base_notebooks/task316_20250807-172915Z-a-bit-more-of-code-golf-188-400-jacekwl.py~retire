def p(m,R=range):
	A=3;B=[]
	for C in R(len(m[0])):
		for D in R(len(m)):
			if m[D][C]:B.append(m[D][C]);break
	B+=[0]*(A*A-len(B));return[B[C*A:(C+1)*A]if C%2==0 else B[C*A:(C+1)*A][::-1]for C in R(A)]