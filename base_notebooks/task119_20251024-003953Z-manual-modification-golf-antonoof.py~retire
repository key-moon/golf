def p(I):
	K=None;E,F=len(I),len(I[0]);C=[list(A)for A in I];O=[(A,B)for A in range(E)for B in range(F)if I[A][B]==2];G=[(A,B)for A in range(E)for B in range(F)if I[A][B]==8]
	if not G or not O:return C
	R={A for(A,B)in O};S={A for(B,A)in O};s=len(R)==E and len(S)>=1;X=len(S)==F and len(R)>=1;from collections import Counter as Y;Z=Y(B-A for(A,B)in G);a=Y(A+B for(A,B)in G);b,U=K,0
	if Z:b,U=Z.most_common(1)[0]
	c,d=K,0
	if a:c,d=a.most_common(1)[0]
	if U>=d and U>0:P=1;l=b
	else:P=-1;l=c
	if X:
		L=min(R)==0
		def e(di):
			D=di if P==1 else-di;L,M=min(G);H=0;I=K;A,B=L+di,M+D
			while 0<=A<E and 0<=B<F:
				if(A,B)in J:break
				if C[A][B]==0:H+=1;I=A,B
				A+=di;B+=D
			return H,I
		J=set(O);m,n=e(1 if L else-1);o,n=e(-1 if L else 1);D=(1 if L else-1)if m>=o else-1 if L else 1;M=D if P==1 else-D
	else:
		T=min(S)>sum(A for(B,A)in G)/len(G)
		if P==1:D=1 if T else-1;M=D
		else:D=-1 if T else 1;M=-D
	f,g=min(G);J=set(O);Q=K;A,B=f+D,g+M
	while 0<=A<E and 0<=B<F:
		if(A,B)in J:break
		if C[A][B]==0:C[A][B]=3;Q=A,B
		A+=D;B+=M
	if Q is K:
		A,B=f+D,g+M;h=K
		while 0<=A<E and 0<=B<F and(A,B)not in J:h=A,B;A+=D;B+=M
		Q=h
	if Q is K:return I
	V,W=Q
	if X:L=min(R)==0;H=1 if L else-1;N=-H if P==1 else H
	else:
		T=min(S)>sum(A for(B,A)in G)/len(G);i=-1 if T else 1;j=-1;k=i;p=1;q=i
		def r(di2_,dj2_):A,B=V+di2_,W+dj2_;return 0<=A<E and 0<=B<F and(A,B)not in J and C[A][B]==0
		if r(j,k):H,N=j,k
		else:H,N=p,q
		A,B=V+H,W+N
		while 0<=A<E and 0<=B<F:
			if(A,B)in J:break
			if C[A][B]==0:C[A][B]=3
			A+=H;B+=N
		return C
	A,B=V+H,W+N
	while 0<=A<E and 0<=B<F:
		if(A,B)in J:break
		if C[A][B]==0:C[A][B]=3
		A+=H;B+=N
	return C