ZERO=0
FOUR=4
def mostcolor(grid):A=[B for A in grid for B in A];return max(set(A),key=A.count)
def ofcolor(grid,value):return{(A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value}
def fill(grid,value,cells):
	B=cells;A=grid
	if not B:return[list(A)for A in A]
	F,G=len(A),len(A[0]);C=[list(A)for A in A]
	for(D,E)in B:
		if 0<=D<F and 0<=E<G:C[D][E]=value
	return C
def bounds(idxs):A=idxs;B=min(A for(A,B)in A);C=min(A for(B,A)in A);D=max(A for(A,B)in A);E=max(A for(B,A)in A);return B,C,D,E
def position(a_idxs,b_idxs):
	E,F,G,H=bounds(a_idxs);I,J,K,L=bounds(b_idxs);A,B=(E+G)//2,(F+H)//2;C,D=(I+K)//2,(J+L)//2
	if A==C:return 0,1 if B<D else-1
	if B==D:return 1 if A<C else-1,0
	if A<C:return 1,1 if B<D else-1
	if A>C:return-1,1 if B<D else-1
	return 0,0
def dneighbors(loc):A,B=loc;return{(A-1,B),(A+1,B),(A,B-1),(A,B+1)}
def connect(a,b):
	A,B=a;C,D=b
	if A==C:E,I=(B,D)if B<=D else(D,B);return{(A,B)for B in range(E,I+1)}
	if B==D:F,J=(A,C)if A<=C else(C,A);return{(A,B)for A in range(F,J+1)}
	G,H=C-A,D-B
	if abs(G)==abs(H):F=1 if G>0 else-1;E=1 if H>0 else-1;K=abs(G);return{(A+C*F,B+C*E)for C in range(0,K+1)}
	return set()
def p(I):
	A0='bottom';z='top'
	if not I or not I[0]:return[list(A)for A in I]
	L,F=len(I),len(I[0]);G=mostcolor(I);S={(A,B)for A in range(L)for B in range(F)if I[A][B]!=G}
	if not S:return[list(A)for A in I]
	D,B,A,C=bounds(S);A1={(A,B)for A in range(D,A+1)}|{(A,C)for A in range(D,A+1)}|{(D,A)for A in range(B,C+1)}|{(A,B)for B in range(B,C+1)};T=A1-S;A2={(A,D)for A in range(D,A+1)for D in range(B,C+1)};P=A2-S;X=position(P,T);Z=position(T,P);A3={z:sum(1 for A in range(B,C+1)if I[D][A]==G),A0:sum(1 for B in range(B,C+1)if I[A][B]==G),'left':sum(1 for A in range(D,A+1)if I[A][B]==G),'right':sum(1 for A in range(D,A+1)if I[A][C]==G)};A4={z:(-1,0),A0:(1,0),'left':(0,-1),'right':(0,1)};M=None;Q=[(A,A4[B])for(B,A)in A3.items()if A]
	if Q:
		Q.sort(key=lambda item:item[0],reverse=True)
		if len(Q)==1 or Q[0][0]>Q[1][0]:M=Q[0][1]
	a=sum(1 for A in range(L)for C in range(0,B)if I[A][C]==ZERO);b=sum(1 for A in range(L)for B in range(C+1,F)if I[A][B]==ZERO);c=sum(1 for A in range(0,D)for B in range(F)if I[A][B]==ZERO);d=sum(1 for A in range(A+1,L)for B in range(F)if I[A][B]==ZERO);H=1 if b>a else-1 if a>b else 0;J=1 if d>c else-1 if c>d else 0
	def e(d):
		B,C=d;A=0
		if H and C==H:A+=1
		if J and B==J:A+=1
		return A
	K=M
	if K is None:
		if X==Z:
			if H==0 and J!=0:K=J,0
			elif J==0 and H!=0:K=0,H
			else:K=X
		else:
			K=max((X,Z),key=e)
			if e(K)==0 and(J or H):
				N=J if J else 0;O=H if H else 0
				if N or O:K=N,O
	N,O=K;Y=set()
	for f in range(0,9):
		A5,A6=N*f,O*f
		for(A7,A8)in T:Y.add((A7+A5,A8+A6))
	R=fill(I,FOUR,P);g=ofcolor(I,ZERO);R=fill(R,FOUR,Y&g)
	if T:h,i,j,k=bounds(T);l={(h,i),(h,k),(j,i),(j,k)}
	else:l={(D,B),(D,C),(A,B),(A,C)}
	U=ofcolor(R,ZERO);N,O=K
	if O==0 and N!=0:U={A for A in U if B<=A[1]<=C}
	elif N==0 and O!=0:U={B for B in U if D<=B[0]<=A}
	A9=J==0 and H==0;AA=I if A9 else R
	def AB(loc):
		A=0
		for(B,C)in dneighbors(loc):
			if 0<=B<L and 0<=C<F and AA[B][C]==ZERO:A+=1
		return A==2
	def m(idxs,loc):return any((A,B)in idxs for(A,B)in dneighbors(loc))
	AC=[A for A in U if AB(A)and m(S,A)and m(Y,A)];n=set()
	for V in l:
		for o in AC:p=o[0]-V[0],o[1]-V[1];AD=V[0]+42*p[0],V[1]+42*p[1];n|=connect(V,AD)
	E=fill(R,FOUR,n&g)
	if M and P:
		q={A for(B,A)in P};r={A for(A,B)in P}
		if M==(-1,0)and D>0:
			s={(D-1,A)for A in q if 0<=A<F and I[D-1][A]==G}
			if s:E=fill(E,FOUR,s)
		elif M==(1,0)and A+1<L:
			t={(A+1,B)for B in q if 0<=B<F and I[A+1][B]==G}
			if t:E=fill(E,FOUR,t)
		elif M==(0,-1)and B>0:
			u={(A,B-1)for A in r if 0<=A<L and I[A][B-1]==G}
			if u:E=fill(E,FOUR,u)
		elif M==(0,1)and C+1<F:
			v={(A,C+1)for A in r if 0<=A<L and I[A][C+1]==G}
			if v:E=fill(E,FOUR,v)
	if M==(1,0):
		AE=any(B not in(ZERO,FOUR)for A in I for B in A);W=A+1
		if AE or 0<=W==len(I)-1:
			w=False
			if 0<=W<len(I):
				AF=range(B+1,C)
				def AG(j):return any(B+1<=D<C and R[A][D]==FOUR for D in(j-1,j,j+1))
				x=tuple(A for A in AF if I[W][A]==ZERO and AG(A))
				if x:AH={(W,A)for A in x};E=fill(E,FOUR,AH);w=True
			if w:
				F=len(I[0]);y={(A,D)for D in range(F)if(D<B or D>C)and E[A][D]==FOUR}
				if y:E=fill(E,ZERO,y)
	return E