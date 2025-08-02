def p(g):
	D=g[0]
	while 1:
		for C in range(100):
			if g[C//10][C%10]==5:B=[C];g[C//10][C%10]=0;break
		else:break
		for A in B:
			if A%10<9 and g[A//10][A%10+1]==5:B+=A+1;g[A//10][A%10+1]=0
			if A%10>0 and g[A//10][A%10-1]==5:B+=A-1;g[A//10][A%10-1]=0
			if A//10<9 and g[A//10+1][A%10]==5:B+=A+10;g[A//10+1][A%10]=0
			if A//10>0 and g[A//10-1][A%10]==5:B+=A-10;g[A//10-1][A%10]=0
		E=next(D[A]for A in range(min(A%10 for A in B),max(A%10 for A in B)+1)if D[A])
		for A in B:g[A//10][A%10]=E
	return g