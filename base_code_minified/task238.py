def p(A):
	E={}
	for(O,P)in enumerate(A):
		for(Q,B)in enumerate(P):
			if B:E.setdefault(B,[]).append([O,Q])
	C=[];D=[]
	for(F,K)in E.items():
		L=[A for(A,B)in K];M=[A for(B,A)in K];G,H=min(L),min(M);I=max(L)-G+1;N=max(M)-H+1
		if I>1 and N>1:B,R,S,T,J=F,G,H,I,N
		elif I==1:C.append((G,F))
		else:D.append((H,F))
	C.sort();D.sort();U=C[0][1];V=C[-1][1];W=D[0][1];X=D[-1][1];return[[0]+[U]*J+[0]]+[[W]+[B if[A+R,C+S]in E[B]else 0 for C in range(J)]for A in range(T)]+[[0]+[V]*J+[0]]