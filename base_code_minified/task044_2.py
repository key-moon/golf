def p(A):
	B=[B for A in A for B in A];U=[1,-1,10,-10]
	def F(A):
		C=[0]*100;F=[]
		for D in range(100):
			if val_u[D]==A and not C[D]:
				E=[D];C[D]=1
				for G in E:
					for H in val_D:
						B=G+H
						if 0<=B<100 and abs(G%10-B%10)<2 and val_u[B]==A and not C[B]:C[B]=1;E.append(B)
				F.append(E)
		return F
	J=F(5);K=[(A,B)for A in set(B)-{0,5}for B in F(A)]
	for G in J:
		H=[A//10 for A in G];I=[A%10 for A in G];L,M=min(H),max(H);N,O=min(I),max(I);C=[10*A+C for A in range(L,M+1)for C in range(N,O+1)if B[10*A+C]==0];P=min(C);Q={A-P for A in C}
		for(R,D)in K:
			S=min(D);T={A-S for A in D}
			if T==Q:
				for E in C:B[E]=R
				for E in D:B[E]=0
				break
	return[B[A*10:(A+1)*10]for A in range(10)]