def p(A):
	E=A[0]
	while 1:
		for D in range(100):
			if A[D//10][D%10]==5:C=[D];A[D//10][D%10]=0;break
		else:break
		for B in C:
			if B%10<9 and A[B//10][B%10+1]==5:C+=B+1;A[B//10][B%10+1]=0
			if B%10>0 and A[B//10][B%10-1]==5:C+=B-1;A[B//10][B%10-1]=0
			if B//10<9 and A[B//10+1][B%10]==5:C+=B+10;A[B//10+1][B%10]=0
			if B//10>0 and A[B//10-1][B%10]==5:C+=B-10;A[B//10-1][B%10]=0
		F=next(E[A]for A in range(min(A%10 for A in C),max(A%10 for A in C)+1)if E[A])
		for B in C:A[B//10][B%10]=F
	return A