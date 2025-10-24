a=len
i=range
q=[[0,1],[0,-1],[1,0],[-1,0]]
def p(n):
	F,G=a(n),a(n[0]);D=sum(n,[]);C=sorted([[D.count(A),A]for A in set(D)])
	for A in i(F):
		for B in i(G):
			if n[A][B]==C[1][1]:
				for(D,I)in q:
					for g in i(20):
						if 0<=A+D*g<F and 0<=B+I*g<G:
							E=n[A+D*g][B+I*g]
							if E==C[0][1]:n[A][B]=0
	for A in range(4):
		n=list(map(list,zip(*n[::-1])));F,G=a(n),a(n[0])
		for A in i(F):
			E=0
			for B in i(G):
				if n[A][B]==C[0][1]and n[A].count(0)>0 and n[A].index(0)>B:E=1
				if E:
					if n[A][B]==C[2][1]:n[A][B]=C[0][1]
					elif n[A][B]==0:E=0
	n=[[C[1][1]if A==0 else A for A in A]for A in n];return n