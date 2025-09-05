def	p(j,A=enumerate):
	c=lambda	E,k:sum([[B,b]for(B,r)in	A(j)for(b,v)in	A(r)if	v	in	E	and	v	not	in	k],[]);B,k,C,l,D,a,E,e=c(range(10),[0,8]);F,w=c([8],[])[:2];j[F][w:w+2]=[j[B][k],j[C][l]][::(1,-1)[k>l]];j[F+1][w:w+2]=[j[D][a],j[E][e]][::(1,-1)[a>e]]
	for(G,b)in(B,k),(C,l),(D,a),(E,e):j[G][b]=0
	return	j