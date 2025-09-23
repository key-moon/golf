from itertools import*
L=len
R=range
P=list(product([0,1,-1],repeat=2))
def p(g):
	h,w=L(g),L(g[0])
	for r in R(h):
		for c in R(w):
			if g[r][c]==2:
				for(y,x)in P:
					if 0<=r+y<h and 0<=c+x<w:
						for z in R(20):
							if 0<=r+y*z<h and 0<=c+x*z<w:
								W=g[r+y*z][c+x*z]
								if W==5 and g[r+y][c+x]==0:g[r+y][c+x]=5;g[r+y*z][c+x*z]=0
	return g