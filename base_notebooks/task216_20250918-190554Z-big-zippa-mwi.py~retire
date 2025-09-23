R=range
L=len
def p(a):
	K,C=L(a),L(a[0]);E=F=M=N=O=P=0
	for G in R(K):
		H=[0]*C;I=[0]*C
		for D in R(G,K):
			H=[A+(B==2)for(A,B)in zip(H,a[D])];I=[A+(B==0)for(A,B)in zip(I,a[D])];B=J=0
			for A in R(C+1):
				if A<C and I[A]==0:B+=H[A]
				else:
					Q=A-J;S=(D-G+1)*Q
					if Q and(B>E or B==E and S>F):E,F,M,N,O,P=B,S,G,J,D,A-1
					J=A+1;B=0
	return[A[N:P+1]for A in a[M:O+1]]if F else[]