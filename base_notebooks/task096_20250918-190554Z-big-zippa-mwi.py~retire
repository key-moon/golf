def mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,(tuple,list))else[A[0]for A in A];return max(set(B),key=B.count)
def neighbors(loc):A,B=loc;return{(A-1,B-1),(A-1,B),(A-1,B+1),(A,B-1),(A,B+1),(A+1,B-1),(A+1,B),(A+1,B+1)}
def asindices(grid):
	A=grid
	if not A or not A[0]:return set()
	return{(B,C)for B in range(len(A))for C in range(len(A[0]))}
def ulcorner(patch):A=toindices(patch);return min(A for(A,B)in A),min(A for(B,A)in A)
def lrcorner(patch):A=toindices(patch);return max(A for(A,B)in A),max(A for(B,A)in A)
def toindices(patch):
	A=patch
	if len(A)==0:return set()
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{A for(B,A)in A}
	return A
def shift(patch,directions):
	A=patch
	if len(A)==0:return A
	C,D=directions;B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B+C,E+D))for(A,(B,E))in A}
	return{(A+C,B+D)for(A,B)in A}
def normalize(patch):
	A=patch
	if len(A)==0:return A
	return shift(A,(-uppermost(A),-leftmost(A)))
def dneighbors(loc):A=loc;return{(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)}
def objects(grid,univalued,diagonal,without_bg):
	A=grid;H=mostcolor(A)if without_bg else None;I=[];D=set();L,M=len(A),len(A[0]);N=asindices(A);O=neighbors if diagonal else dneighbors
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while F:
			K=set()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if univalued else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.append(J)
	return I
def fgpartition(grid):A=grid;B=mostcolor(A);return[{(A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B}for B in palette(A)-{B}]
def uppermost(patch):return min(A for(A,B)in toindices(patch))
def leftmost(patch):return min(A for(B,A)in toindices(patch))
def rightmost(patch):return max(A for(B,A)in toindices(patch))
def manhattan(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in toindices(a)for(C,D)in toindices(b))
def palette(element):
	A=element
	if isinstance(A,(tuple,list)):return{B for A in A for B in A}
	return{A[0]for A in A}
def rot90(grid):return[list(A)for A in zip(*grid[::-1])]
def hmirror(piece):
	A=piece;C=ulcorner(A)[0]+lrcorner(A)[0];B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(C-B,D))for(A,(B,D))in A}
	return{(C-A,B)for(A,B)in A}
def vmirror(piece):
	A=piece;C=ulcorner(A)[1]+lrcorner(A)[1];B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B,C-D))for(A,(B,D))in A}
	return{(A,C-B)for(A,B)in A}
def dmirror(piece):
	A=piece;B,C=ulcorner(A);D=next(iter(A))
	if isinstance(D,tuple)and len(D)==2 and isinstance(D[1],tuple):return{(A,(E-C+B,D-B+C))for(A,(D,E))in A}
	return{(D-C+B,A-B+C)for(A,D)in A}
def cmirror(piece):return vmirror(dmirror(vmirror(piece)))
def paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=[list(A)for A in A]
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return B
def canvas(value,dimensions):A=dimensions;return[[value for A in range(A[1])]for B in range(A[0])]
def solve_4290ef0e(I):
	if not isinstance(I,tuple):I=tuple(tuple(A)for A in I)
	G=mostcolor(I);B=fgpartition(I);H=objects(I,True,False,True)
	def J(area):
		D=next(iter(area))[0];A=[A for A in H if next(iter(A))[0]==D]
		if A:B=max((rightmost(A)-leftmost(A)+1 for A in A),default=0)
		else:B=0
		E={manhattan(C,B)for B in A for C in A};F={A for A in E if A!=0};C=min(F,default=0);G=C-1 if C>0 else-2;return-(2*B+G)
	K=sorted(B,key=J)
	def L(area):
		A=area
		def B(piece):return tuple(sorted(toindices(normalize(piece))))
		C=vmirror(A),dmirror(A),cmirror(A),hmirror(A);return min(C,key=B)
	M=[L(A)for A in K];N=tuple(normalize(A)for A in M);C=len(B);D=C if any(len(A)==1 for A in B)else C+1;O=tuple((A,A)for A in range(D));E=tuple(C for(A,B)in zip(N,O)for C in sorted(shift(A,B),key=lambda t:t[1]));F=2*D-1;A=canvas(G,(F,F))
	for P in range(3):A=paint(A,E);A=rot90(A)
	A=paint(A,E);return A
def p(g):return solve_4290ef0e(g)