_A=False
from collections import Counter
def mostcolor(g):
	if not g or not g[0]:return 0
	A=Counter(B for A in g for B in A);C=max(A.values());B=[A for(A,B)in A.items()if B==C];return 0 if 0 in B else min(B)
def objects(g,u=_A,d=_A,w=True):
	if not g or not g[0]:return[]
	H,I=len(g),len(g[0]);J=mostcolor(g)if w else None;D=[[0]*I for A in range(H)];N=[];P=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*d
	for E in range(H):
		for F in range(I):
			C=g[E][F]
			if D[E][F]or w and C==J:continue
			O=C if u else None;G=[(E,F)];D[E][F]=1;K=[]
			while G:
				L,M=G.pop();C=g[L][M]
				if u and C!=O or not u and w and C==J:continue
				K.append((C,(L,M)))
				for(Q,R)in P:
					A,B=L+Q,M+R
					if 0<=A<H and 0<=B<I and not D[A][B]:
						if u:
							if g[A][B]==O:D[A][B]=1;G.append((A,B))
						elif not(w and g[A][B]==J):D[A][B]=1;G.append((A,B))
			if K:N.append(K)
	return N
def bbox(o):E=iter(o);H,(F,G)=next(E);A=B=F;C=D=G;[((A:=min(A,E)),(B:=max(B,E)),(C:=min(C,F)),(D:=max(D,F)))for(G,(E,F))in E];return A,C,B,D
def normalize(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(B-mi,C-mj))for(A,(B,C))in o])(*bbox(o))
def shift(o,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in o]
def vmirror(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(B,mj+mj2-C))for(A,(B,C))in o])(*bbox(o))
def hmirror(o):return o if not o else(lambda mi,mj,mi2,mj2:[(A,(mi+mi2-B,C))for(A,(B,C))in o])(*bbox(o))
def dmirror(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(C-mj+mi,B-mi+mj))for(A,(B,C))in o])(*bbox(o))
def cmirror(o):return vmirror(dmirror(vmirror(o)))
def paint(g,o):
	if not g or not g[0]:return g
	D,E=len(g),len(g[0]);A=[list(A)for A in g]
	for(F,(B,C))in o:
		if 0<=B<D and 0<=C<E:A[B][C]=F
	return A
def occurrences(g,o):
	if not g or not g[0]:return set()
	B,D=len(g),len(g[0]);A=normalize(o)
	if not A:return set()
	C,E,F,G=bbox(A);H,I=F-C+1,G-E+1;return{(B,C)for B in range(B-H+1)for C in range(D-I+1)if all(g[B][C]==A for(A,(B,C))in shift(A,(B,C)))}
def p(I):
	C=objects(I,u=_A,d=True,w=True)
	if not C:return I
	F=max(C,key=lambda o:len({A for(A,B)in o}));B=[cmirror,dmirror,hmirror,vmirror];G=B+[lambda x,a=A,b=C:a(b(x))for A in B for C in B];D=[]
	for H in G:
		J=H(F);E=normalize(J);A=[(A,(B,C))for(A,(B,C))in E if A in{2,4}]
		if not A:continue
		K,L=min(B for(A,(B,A))in A),min(B for(A,(A,B))in A)
		for(M,N)in occurrences(I,A):D.append(shift(E,(M-K,N-L)))
	return paint(I,{B for A in D for B in A})