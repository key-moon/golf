def p(A):
	B=len(A)
	if len({*sum(A,[])})<3:return[[A[C<B and C or 2*B-1-C][D<B and D or 2*B-1-D]for D in range(2*B)]for C in range(2*B)]
	C=lambda x:[list(A)for A in zip(*x[::-1])];return[A+B for(A,B)in zip(A,C(A))]+[A+B for(A,B)in zip(C(C(C(A))),C(C(A)))]