def p(val_g):
	A=[B for A in val_g for B in A];I=[1,-1,10,-10]
	def E(val_c):
		F=val_c;C=[0]*100;G=[]
		for D in range(100):
			if A[D]==F and not C[D]:
				E=[D];C[D]=1
				for H in E:
					for J in I:
						B=H+J
						if 0<=B<100 and abs(H%10-B%10)<2 and A[B]==F and not C[B]:C[B]=1;E.append(B)
				G.append(E)
		return G
	J=E(5);K=[(A,B)for A in set(A)-{0,5}for B in E(A)]
	for F in J:
		G=[A//10 for A in F];H=[A%10 for A in F];L,M=min(G),max(G);N,O=min(H),max(H);B=[10*B+C for B in range(L,M+1)for C in range(N,O+1)if A[10*B+C]==0];P=min(B);Q={A-P for A in B}
		for(R,C)in K:
			S=min(C);T={A-S for A in C}
			if T==Q:
				for D in B:A[D]=R
				for D in C:A[D]=0
				break
	return[A[B*10:(B+1)*10]for B in range(10)]