_A=None
from typing import*
from copy import*
Point=Tuple[int,int]
Grid=List[List[int]]
def i1(g,r,c):return 0<=r<len(g)and 0<=c<len(g[0])
def n4(r,c):return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def l1(d):return 0 if d[0]==0 else 1 if d[0]>0 else-1,0 if d[1]==0 else 1 if d[1]>0 else-1
def r1(d):return-d[1],d[0]
def r2(d):return d[1],-d[0]
def l2(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def с1(g,val):return[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==val]
def c4(g,positions):
	A=set(positions);E=[]
	while A:
		F=A.pop();D=[F];G=[F]
		while D:
			H,I=D.pop()
			for(B,C)in n4(H,I):
				if(B,C)in A:A.remove((B,C));D.append((B,C));G.append((B,C))
		E.append(G)
	return E
def c(goals,p):A=goals;return min(l2(p,A)for A in A)if A else 10**9
def i(val):return val==0 or val==3
class RunInfo:
	__slots__='pred','path','steps','dmin','dend','bounces','start','start_dir'
	def __init__(A,pred,path,steps,dmin,dend,bounces,start,start_dir):A.pred=pred;A.path=path;A.steps=steps;A.dmin=dmin;A.dend=dend;A.bounces=bounces;A.start=start;A.start_dir=start_dir
def r(g,start,d,reds):
	M=start;J=reds;T,U=len(g),len(g[0]);C=deepcopy(g);G=set();K=0;A=M;D=d;N=[A];H=c(J,A);O=H;L=0
	while K<T*U*10:
		K+=1;F=add(A,D)
		if i1(g,*F)and C[F[0]][F[1]]==2:break
		V=not i1(g,*F)or not i(C[F[0]][F[1]])
		if not V:
			A=F
			if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
			E=A,D
			if E in G:break
			G.add(E)
		else:
			P,W=r1(D),r2(D);I=[]
			for Q in(P,W):
				B=add(A,Q)
				if i1(g,*B)and i(C[B[0]][B[1]]):I.append((c(J,B),Q,B))
			if I:
				I.sort(key=lambda x:(x[0],0 if x[1]==P else 1));Y,X,B=I[0];D=X;A=B
				if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
				E=A,D
				if E in G:break
				G.add(E);L+=1
			else:
				R=-D[0],-D[1];B=add(A,R)
				if i1(g,*B)and i(C[B[0]][B[1]]):
					D=R;A=B
					if C[A[0]][A[1]]==0:C[A[0]][A[1]]=3
					E=A,D
					if E in G:break
					G.add(E);L+=1
				else:break
		N.append(A);S=c(J,A);H=min(H,S);O=S
	return RunInfo(C,N,K,H,O,L,M,d)
def s(g):
	D=с1(g,2);G=с1(g,3)
	if not D or not G:return deepcopy(g)
	P=c4(g,G);E=min(P,key=lambda comp:(len(comp),c(D,(round(sum(A for(A,B)in comp)/len(comp)),round(sum(A for(B,A)in comp)/len(comp))))));A=_A;Q=set(E)
	for(H,I)in E:
		for(J,K)in n4(H,I):
			if(J,K)in Q:A=(H,I),(J,K);break
		if A:break
	if A is _A:
		L=_A;M=-1
		for B in E:
			for C in E:
				N=l2(B,C)
				if N>M:L=B,C;M=N
		A=L
	B,C=A;F=l1(sub(C,B));O=[r(g,C,F,D),r(g,B,(-F[0],-F[1]),D)];O.sort(key=lambda r:(r.dend,r.bounces,r.dmin,r.steps));return O[0].pred
def d(g):
	D=с1(g,2);E=с1(g,3)
	if len(D)!=2 or len(E)!=2:return
	def H(ps):(A,B),(C,D)=sorted(ps);return B==D and abs(A-C)==1
	if not(H(D)and H(E)):return
	(I,F),(J,P)=sorted(E);(K,G),(L,P)=sorted(D)
	if{I,J}!={K,L}:return
	M,N=sorted([F,G]);C=_A
	for A in range(0,min(I,K)+1):
		if all(g[A][B]in(0,3,2)for B in range(M,N+1)):C=A;break
	if C is _A or C==0:return
	B=deepcopy(g);Q=max(J,L)
	for A in range(C,Q+1):
		if B[A][F]==0:B[A][F]=3
		if B[A][G]==0:B[A][G]=3
	for O in range(M,N+1):
		if B[C][O]==0:B[C][O]=3
	return B
def p(grid):
	A=d(grid)
	if A is not _A:return A
	return s(grid)