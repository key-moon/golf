r=range
L=len
def p(a):
	M=False;t=None;J,K=L(a),L(a[0]);u=[[1 if a[x][f]else 0 for f in r(3)]for x in r(3)]
	for x in r(J-2):
		for f in r(K-2):
			if x<1 and f<1:continue
			C=t;n=True
			for i in r(3):
				for d in r(3):
					G=a[x+i][f+d]
					if u[i][d]:
						if not G or C is not t and G!=C:n=M;break
						if C is t:C=G
					elif G:n=M;break
				if not n:break
			if not n:continue
			if any(0<=x+i+n<J and 0<=f+d+G<K and not(x<=x+i+n<x+3 and f<=f+d+G<f+3)and a[x+i+n][f+d+G]==C for i in r(3)for d in r(3)if u[i][d]for(n,G)in((1,0),(-1,0),(0,1),(0,-1))):continue
			for i in r(3):
				for d in r(3):
					if u[i][d]:a[x+i][f+d]=5
			return a
	return a