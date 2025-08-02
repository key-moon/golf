def p(A):
	D=A[0][5];E=[(B,C)for B in range(5)for C in range(5)if A[B][C]]
	for B in range(3):
		for C in range(3):
			if B!=C:
				for(F,G)in E:A[B*6+F][C*6+G]=D
	return A