def p(g):
	K=len(g);G=len(g[0]);H=[];L=0
	for A in range(K):
		for B in range(G):
			if g[A][B]:
				M=g[A][B];I=[(A,B)];g[A][B]=0;J=[]
				while I:
					C,D=I.pop();J.append((C,D))
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						E=C+O;F=D+P
						if 0<=E<K and 0<=F<G and g[E][F]==M:g[E][F]=0;I.append((E,F))
				if len(J)>len(H):H=J;L=M
	N=[[0]*G for A in g]
	for(C,D)in H:N[C][D]=L
	return N