_A=None
from typing import List,Tuple,Optional
from copy import deepcopy
Point=Tuple[int,int]
Grid=List[List[int]]
GREEN,RED,BG=3,2,0
def in_bounds(g,r,c):return 0<=r<len(g)and 0<=c<len(g[0])
def neighbors4(r,c):return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def norm1(d):return 0 if d[0]==0 else 1 if d[0]>0 else-1,0 if d[1]==0 else 1 if d[1]>0 else-1
def rotate_left(d):return-d[1],d[0]
def rotate_right(d):return d[1],-d[0]
def manhattan(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def find_positions(g,val):return[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==val]
def comp_4_connected(g,positions):
	A=set(positions);E=[]
	while A:
		F=A.pop();D=[F];G=[F]
		while D:
			H,I=D.pop()
			for(B,C)in neighbors4(H,I):
				if(B,C)in A:A.remove((B,C));D.append((B,C));G.append((B,C))
		E.append(G)
	return E
def closest_goal_distance(goals,p):A=goals;return min(manhattan(p,A)for A in A)if A else 10**9
def is_free_for_path(val):return val==BG or val==GREEN
def choose_start_and_dir(g,greens,reds):
	F=greens
	if not F or not reds:return
	M=comp_4_connected(g,F);E=min(M,key=lambda comp:(len(comp),closest_goal_distance(reds,(round(sum(A for(A,B)in comp)/len(comp)),round(sum(A for(B,A)in comp)/len(comp))))));B=_A;N=set(E)
	for(G,H)in E:
		for(I,J)in neighbors4(G,H):
			if(I,J)in N:B=(G,H),(I,J);break
		if B:break
	if B is _A:
		K=_A;L=-1
		for C in E:
			for D in E:
				A=manhattan(C,D)
				if A>L:K=C,D;L=A
		B=K
	C,D=B;A=norm1(sub(D,C));O=[(D,A),(C,(-A[0],-A[1]))];return min(O,key=score)
class RunInfo:
	__slots__='pred','path','steps','dmin','dend','bounces','start','start_dir'
	def __init__(A,pred,path,steps,dmin,dend,bounces,start,start_dir):A.pred=pred;A.path=path;A.steps=steps;A.dmin=dmin;A.dend=dend;A.bounces=bounces;A.start=start;A.start_dir=start_dir
def run_with_start(g,start,d,reds):
	M=start;J=reds;T,U=len(g),len(g[0]);C=deepcopy(g);G=set();K=0;A=M;D=d;N=[A];H=closest_goal_distance(J,A);O=H;L=0
	while K<T*U*10:
		K+=1;F=add(A,D)
		if in_bounds(g,*F)and C[F[0]][F[1]]==RED:break
		V=not in_bounds(g,*F)or not is_free_for_path(C[F[0]][F[1]])
		if not V:
			A=F
			if C[A[0]][A[1]]==BG:C[A[0]][A[1]]=GREEN
			E=A,D
			if E in G:break
			G.add(E)
		else:
			P,W=rotate_left(D),rotate_right(D);I=[]
			for Q in(P,W):
				B=add(A,Q)
				if in_bounds(g,*B)and is_free_for_path(C[B[0]][B[1]]):I.append((closest_goal_distance(J,B),Q,B))
			if I:
				I.sort(key=lambda x:(x[0],0 if x[1]==P else 1));Y,X,B=I[0];D=X;A=B
				if C[A[0]][A[1]]==BG:C[A[0]][A[1]]=GREEN
				E=A,D
				if E in G:break
				G.add(E);L+=1
			else:
				R=-D[0],-D[1];B=add(A,R)
				if in_bounds(g,*B)and is_free_for_path(C[B[0]][B[1]]):
					D=R;A=B
					if C[A[0]][A[1]]==BG:C[A[0]][A[1]]=GREEN
					E=A,D
					if E in G:break
					G.add(E);L+=1
				else:break
		N.append(A);S=closest_goal_distance(J,A);H=min(H,S);O=S
	return RunInfo(C,N,K,H,O,L,M,d)
def dual_start_solver(g):
	D=find_positions(g,RED);G=find_positions(g,GREEN)
	if not D or not G:return deepcopy(g)
	P=comp_4_connected(g,G);E=min(P,key=lambda comp:(len(comp),closest_goal_distance(D,(round(sum(A for(A,B)in comp)/len(comp)),round(sum(A for(B,A)in comp)/len(comp))))));A=_A;Q=set(E)
	for(H,I)in E:
		for(J,K)in neighbors4(H,I):
			if(J,K)in Q:A=(H,I),(J,K);break
		if A:break
	if A is _A:
		L=_A;M=-1
		for B in E:
			for C in E:
				N=manhattan(B,C)
				if N>M:L=B,C;M=N
		A=L
	B,C=A;F=norm1(sub(C,B));O=[run_with_start(g,C,F,D),run_with_start(g,B,(-F[0],-F[1]),D)];O.sort(key=lambda r:(r.dend,r.bounces,r.dmin,r.steps));return O[0].pred
def detect_and_solve_top_bridge_refined(g):
	D=find_positions(g,RED);E=find_positions(g,GREEN)
	if len(D)!=2 or len(E)!=2:return
	def H(ps):(A,B),(C,D)=sorted(ps);return B==D and abs(A-C)==1
	if not(H(D)and H(E)):return
	(I,F),(J,P)=sorted(E);(K,G),(L,P)=sorted(D)
	if{I,J}!={K,L}:return
	M,N=sorted([F,G]);C=_A
	for A in range(0,min(I,K)+1):
		if all(g[A][B]in(BG,GREEN,RED)for B in range(M,N+1)):C=A;break
	if C is _A or C==0:return
	B=deepcopy(g);Q=max(J,L)
	for A in range(C,Q+1):
		if B[A][F]==BG:B[A][F]=GREEN
		if B[A][G]==BG:B[A][G]=GREEN
	for O in range(M,N+1):
		if B[C][O]==BG:B[C][O]=GREEN
	return B
def p(grid):
	A=detect_and_solve_top_bridge_refined(grid)
	if A is not _A:return A
	return dual_start_solver(grid)
