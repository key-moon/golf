def n(i,r):return len(set([A[r]for A in i]))
def p(a):
	C=enumerate;D=n(a,0)+n(a,-1)<len(set(a[0]))+len(set(a[-1]))
	for(A,E)in C(a):
		for(B,E)in C(E):
			if D:a[A][B]=max([a[0][B],a[-1][B]])
			else:a[A][B]=max([a[A][0],a[A][-1]])
	if D:a=[[A for A in A if A>0]for A in a];a=a[:len(a[0])]
	else:a=[A for A in a if sum(A)>0];a=[A[:len(a)]for A in a]
	return a