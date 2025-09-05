j=len
A=range
def p(c):
	E=[[0,0,0]for l in A(3)];k,W=j(c),j(c[0])
	for l in A(k):
		for J in A(W):
			if c[l][J]==5:
				for a in A(-1,2):
					for C in A(-1,2):
						if l+a>=0 and J+C>=0 and c[l+a][J+C]!=0:E[1+a][1+C]=c[l+a][J+C]
	return E