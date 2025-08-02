def p(A):
 for B in range(len(A)-1):A[B][-1-B]=2
 A[-1][1:]=[4]*(len(A)-1);return A