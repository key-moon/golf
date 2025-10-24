def p(o,e=len,p=range):
	D,E,C,e=e(o),e(o[0]),[],[]
	for A in p(D//2+1):
		for B in p(E):
			if o[A][B]==0:e+=[B]
	for A in p(D):
		for B in p(E//2+1):
			if o[A][B]==0:o[A][B]=o[A][-(B+1)];C+=[A]
			if o[A][-(B+1)]==0:o[A][-(B+1)]=o[A][B];C+=[A]
	o=o[min(C):max(C)+1];o=[A[min(e):max(e)+1]for A in o];return o
