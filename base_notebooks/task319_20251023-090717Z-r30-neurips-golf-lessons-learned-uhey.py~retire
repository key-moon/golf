def p(n):
	t=sum(n,[]);H=max(t,key=t.count);A={}
	for(E,g)in enumerate(n):
		for(F,I)in enumerate(g):I-H and A.setdefault(I,set()).add((E,F))
	B=lambda g:(lambda x,y:(min(x),min(y),max(x),max(y)))(*zip(*g));J=lambda g:{(A-B(g)[0],t-B(g)[1])for(A,t)in g};K=max(A,key=lambda m:len(A[m]));o=J(A[K]);M=();D=range;T,t,l,V=B(o)
	for m in A:
		if m-K:
			N=A[m];O={(A*2+t,B*2+E)for(A,B)in J(N)for t in D(2)for E in D(2)};W,X,Y,a=B(O);i=max(len({(t+A,D+B)for(t,D)in O}&o)for A in D(T-Y,l-W+1)for B in D(t-a,V-X+1));P=len(N);Q=i-2*P,P
			if Q>M:M=Q;R=m
	E,F,p,c=B(A[R]);return[[(H,A)[A==R]for A in A[F:c+1]]for A in n[E:p+1]]