from collections import deque
def p(g):
	E,F=len(g),len(g[0]);G=[[0]*F for A in range(E)];K={}
	for H in range(E):
		for I in range(F):
			if not G[H][I]:
				P=g[H][I];L=deque([(H,I)]);G[H][I]=1;Q=[]
				while L:
					A,B=L.popleft();Q.append((A,B))
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=A+M,B+N
						if 0<=C<E and 0<=D<F and not G[C][D]and g[C][D]==P:G[C][D]=1;L.append((C,D))
				K.setdefault(P,[]).append(set(Q))
	R=[A for A in K.get(9,[])if not any(A==0 or B==0 or A==E-1 or B==F-1 for(A,B)in A)];S=set()
	for J in R:S|=J
	T=[A[:]for A in g];U=K.get(1,[])
	if U and R:
		V=S
		for J in U:
			O=False
			for(A,B)in J:
				for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
					if(A+M,B+N)in V:O=True;break
				if O:break
			if O:
				for(A,B)in J:T[A][B]=8
	return T