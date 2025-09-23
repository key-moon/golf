def p(b):
	l=[o[:]for o in b];x,e=len(l),len(l[0]);F=None;b=-1
	for o in range(2,min(9,x)+1):
		for d in range(2,min(9,e)+1):
			for f in range(0,x-o+1):
				for a in range(0,e-d+1):
					c=True
					for q in range(f,f+o):
						i=l[q]
						if any(i[o]!=0 for o in range(a,a+d)):c=False;break
					if c and o*d>b:b=o*d;F=f,a,o,d
	if F:
		f,a,o,d=F
		for q in range(f,f+o):
			for o in range(a,a+d):l[q][o]=6
	return l