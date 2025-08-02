def p(A):
	M,N=len(A),len(A[0]);F={(B,C)for B in range(M)for C in range(N)if A[B][C]}
	if not F:return A
	O=[(1,0),(-1,0),(0,1),(0,-1)];S=[A for A in F if sum((A[0]+B,A[1]+C)in F for(B,C)in O)==1];P,E=S;from collections import deque;H=deque([P]);I={P:None}
	while H:
		B=H.popleft()
		if B==E:break
		for(J,K)in O:
			G=B[0]+J,B[1]+K
			if G in F and G not in I:I[G]=B;H.append(G)
	C=[];B=E
	while B:C.append(B);B=I[B]
	C=C[::-1];Q=[(C[A+1][0]-C[A][0],C[A+1][1]-C[A][1])for A in range(len(C)-1)];T=A[E[0]][E[1]];L=E;R=0
	while True:
		J,K=Q[R%len(Q)];D=L[0]+J,L[1]+K
		if not(0<=D[0]<M and 0<=D[1]<N):break
		if A[D[0]][D[1]]!=0:break
		A[D[0]][D[1]]=T;L=D;R+=1
	return A