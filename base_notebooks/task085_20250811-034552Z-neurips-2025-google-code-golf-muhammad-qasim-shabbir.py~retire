def p(j,A=range):
	c=[k[:]for k in j];E=set()
	for k in A(len(j)-2):
		for W in A(len(j[0])):
			if j[k][W]and(k,W)not in E:
				l=j[k][W]
				if all(j[k+J][W]==l for J in A(3)):
					J=W
					while J<len(j[0])and all(j[k+W][J]==l for W in A(3)):
						for a in A(3):E.add((k+a,J))
						J+=1
					for C in A(W,J):
						if(C-W)%2==1:c[k+1][C]=0
	return c