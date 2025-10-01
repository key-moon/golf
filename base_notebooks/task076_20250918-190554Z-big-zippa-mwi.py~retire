_B=False
_A=True
from collections import Counter
def mostcolor(g):
	if not g or not g[0]:return 0
	A=Counter(B for A in g for B in A);C=max(A.values());B=[A for(A,B)in A.items()if B==C];return 0 if 0 in B else min(B)
def objects(g,univalued=_B,diagonal=_B,without_bg=_A):
	F=without_bg;E=univalued
	if not g or not g[0]:return[]
	J,K=len(g),len(g[0]);L=mostcolor(g)if F else None;D=[[_B]*K for A in range(J)];P=[];R=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*diagonal
	for G in range(J):
		for H in range(K):
			C=g[G][H]
			if D[G][H]or F and C==L:continue
			Q=C if E else None;I=[(G,H)];D[G][H]=_A;M=[]
			while I:
				N,O=I.pop();C=g[N][O]
				if E and C!=Q or not E and F and C==L:continue
				M.append((C,(N,O)))
				for(S,T)in R:
					A,B=N+S,O+T
					if 0<=A<J and 0<=B<K and not D[A][B]:
						if E:
							if g[A][B]==Q:D[A][B]=_A;I.append((A,B))
						elif not(F and g[A][B]==L):D[A][B]=_A;I.append((A,B))
			if M:P.append(M)
	return P
def bbox(o):
	G=iter(o);H,(I,J)=next(G);C=D=I;E=F=J
	for(H,(A,B))in G:
		if A<C:C=A
		elif A>D:D=A
		if B<E:E=B
		elif B>F:F=B
	return C,E,D,F
def normalize(o):
	if not o:return o
	A,B,C,C=bbox(o);return[(C,(D-A,E-B))for(C,(D,E))in o]
def shift(o,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in o]
def vmirror(o):
	if not o:return o
	A,B,A,C=bbox(o);return[(A,(D,B+C-E))for(A,(D,E))in o]
def hmirror(o):
	if not o:return o
	A,B,C,B=bbox(o);return[(B,(A+C-D,E))for(B,(D,E))in o]
def dmirror(o):
	if not o:return o
	A,B,C,C=bbox(o);return[(C,(E-B+A,D-A+B))for(C,(D,E))in o]
def cmirror(o):return vmirror(dmirror(vmirror(o)))
def paint(g,o):
	if not g or not g[0]:return g
	D,E=len(g),len(g[0]);A=[list(A)for A in g]
	for(F,(B,C))in o:
		if 0<=B<D and 0<=C<E:A[B][C]=F
	return A
def occurrences(g,o):
	if not g or not g[0]:return set()
	E,F=len(g),len(g[0]);A=normalize(o)
	if not A:return set()
	G,H,I,J=bbox(A);K=I-G+1;L=J-H+1;B=set()
	for C in range(E-K+1):
		for D in range(F-L+1):
			if all(g[B][C]==A for(A,(B,C))in shift(A,(C,D))):B.add((C,D))
	return B
def solve_36d67576(I):
	if not I or not I[0]:return I
	C=objects(I,univalued=_B,diagonal=_A,without_bg=_A)
	if not C:return I
	F=max(C,key=lambda o:len({A for(A,B)in o}));B=[cmirror,dmirror,hmirror,vmirror];G=B+[lambda x,a=A,b=C:a(b(x))for A in B for C in B];D=[]
	for H in G:
		J=H(F);E=normalize(J);A=[(A,(B,C))for(A,(B,C))in E if A in{2,4}]
		if not A:continue
		K=min(B for(A,(B,A))in A);L=min(B for(A,(A,B))in A)
		for(M,N)in occurrences(I,A):D.append(shift(E,(M-K,N-L)))
	return paint(I,{B for A in D for B in A})
p=solve_36d67576