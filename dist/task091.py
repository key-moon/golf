E=enumerate
B=max
A=min
def	p(g):H=[(i,j)for(i,r)in	E(g)for(j,v)in	E(r)if	v==5];F,G=zip(*H);C,D=A(F)-1,B(F)+1;C,K=B(C,0),None;D,L=A(D,len(g)-1),None;I,J=A(G),B(G);return[A[I:J+1]for	A	in	g[C:D+1]]