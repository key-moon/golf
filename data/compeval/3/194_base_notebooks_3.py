def p(g):
	B=[];C=[list(A)for A in zip(*g[::-1])];D=[list(A)for A in zip(*C[::-1])];E=[list(A)for A in zip(*D[::-1])]
	for A in range(len(g)):B.append(g[A]+C[A])
	for A in range(len(g)):B.append(E[A]+D[A])
	return B