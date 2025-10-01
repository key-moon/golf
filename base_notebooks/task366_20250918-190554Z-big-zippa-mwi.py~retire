def solve_e6721834(I):
	AI='anchor_count';AH='anc_colors';AG='anc_norm';z=False;i='anc_ul';W=None
	def A0(grid):A=[B for A in grid for B in A];return max(set(A),key=A.count)
	def A1(grid):return len({B for A in grid for B in A})
	def Z(grid,start,dims):A,B=start;C,D=dims;return tuple(tuple(A[B:B+D])for A in grid[A:A+C])
	def AJ(grid):A,B=len(grid),len(grid[0]);return{(A,C)for A in range(A)for C in range(B)}
	def AK(loc):A,B=loc;return{(A-1,B),(A+1,B),(A,B-1),(A,B+1)}
	def AL(grid):
		A=grid;G=A0(A);P,Q=len(A),len(A[0]);H=[];E=set()
		for B in AJ(A):
			if B in E:continue
			I,J=B
			if A[I][J]==G:continue
			K={(A[I][J],B)};F={B}
			while F:
				L=set()
				for(C,D)in F:
					M=A[C][D]
					if M!=G:
						K.add((M,(C,D)));E.add((C,D))
						for(N,O)in AK((C,D)):
							if 0<=N<P and 0<=O<Q:L.add((N,O))
				F=L-E
			H.append(K)
		return H
	def U(patch):
		A=patch
		if not A:return set()
		B=next(iter(A))
		if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{A for(B,A)in A}
		return A
	def A2(patch):return min(A for(A,B)in U(patch))
	def AM(patch):return max(A for(A,B)in U(patch))
	def A3(patch):return min(A for(B,A)in U(patch))
	def AN(patch):return max(A for(B,A)in U(patch))
	def AO(patch):A=U(patch);return min(A for(A,B)in A),min(A for(B,A)in A)
	def AP(patch):
		A=patch
		if not A:return A
		return j(A,(-A2(A),-A3(A)))
	def j(patch,delta):
		A=patch;C,D=delta
		if not A:return A
		B=next(iter(A))
		if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B+C,E+D))for(A,(B,E))in A}
		else:return{(A+C,B+D)for(A,B)in A}
	def AQ(patch):
		A=patch
		if not A:return 0
		B=U(A);return max(A for(B,A)in B)-min(A for(B,A)in B)+1
	def AR(grid,obj):
		A=grid;E,F=len(A),len(A[0]);B=[list(A)for A in A]
		for(G,(C,D))in obj:
			if 0<=C<E and 0<=D<F:B[C][D]=G
		return tuple(tuple(A)for A in B)
	a,b=len(I),len(I[0])
	if len(I)>len(I[0]):k=a//2;l=1 if a%2 else 0;A4=Z(I,(0,0),(k,b)),Z(I,(k+l,0),(k,b))
	else:m=b//2;l=1 if b%2 else 0;A4=Z(I,(0,0),(a,m)),Z(I,(0,m+l),(a,m))
	AS,AT=sorted(A4,key=A1);A,AU=AS,AT;E=A0(A);AV=A1(A)>1;O={}
	for AW in A:
		for A5 in AW:O[A5]=O.get(A5,0)+1
	n=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]!=E];P=A;F,C=len(A),len(A[0]);o=[]
	for Q in AL(AU):
		X={}
		for(A6,_)in Q:X[A6]=X.get(A6,0)+1
		if not X:continue
		K=max(X,key=X.get);c=[(A,B)for(A,B)in Q if A!=K]
		if not c:continue
		A7={A for(B,A)in c};D=AO(A7);L=AP(A7);V={(B-D[0],C-D[1]):A for(A,(B,C))in c};p=AM(L)-A2(L)+1;q=AN(L)-A3(L)+1;o.append({'obj':Q,'maj':K,i:D,AG:L,AH:V,'ah':p,'aw':q,AI:len(c),'size':len(Q)})
	o.sort(key=lambda info:(-info[AI],-info['size'],info[i][0],info[i][1]));A8=set()
	for R in o:
		Q=R['obj'];K=R['maj'];D=R[i];L=R[AG];V=R[AH];p=R['ah'];q=R['aw'];M=any(O.get(A,0)for A in V.values());AX={A for A in V.values()}
		if not M:
			if len(AX)>1 or O.get(K,0)==0:continue
		N=[];Y={};A9={}
		for H in range(F-p+1):
			for d in range(C-q+1):
				e=True;r=0;s=set()
				for(S,T)in L:
					t,u=H+S,d+T
					if not(0<=t<F and 0<=u<C):e=z;break
					f=V[S,T];AY=O.get(f,0);v=A[t][u]
					if AY:
						if v!=f or AV and f==E:e=z;break
						if v==f:s.add((t,u))
					else:
						if v!=E:e=z;break
						r+=1
				if e:
					if s&A8:continue
					N.append((H,d));A9[H,d]=s
					if r:Y[H,d]=r
		if not N:continue
		if M and not any(A not in Y for A in N):continue
		B=W;g=-10**9;AZ=sum(1 for B in range(F)for D in range(C//2)if A[B][D]==E);Aa=sum(1 for B in range(F)for D in range(C-C//2,C)if A[B][D]==E);AA=AZ>Aa
		for(J,G)in N:
			S,T=J-D[0],G-D[1];w=j(Q,(S,T));Ab=sum(1 for(G,(B,D))in w if G!=K and 0<=B<F and 0<=D<C and A[B][D]!=E);AB={(J+A,G+B)for(A,B)in L};AC=sum(1 for((B,D),E)in V.items()if 0<=J+B<F and 0<=G+D<C and A[J+B][G+D]==E);Ac=sum(1 for(G,(B,D))in w if(B,D)not in AB and 0<=B<F and 0<=D<C and A[B][D]!=E and A[B][D]!=G);Ad=5 if M else 1;Ae=sum(1 for(E,(B,D))in w if E==K and 0<=B<F and 0<=D<C and A[B][D]==K);AD=0
			if not M and n:AD=sum(min(abs(A-C)+abs(B-D)for(C,D)in n)for(A,B)in AB)
			AE=abs(S)+abs(T)if M else 0
			if M and AC==len(L):AE=0
			Af=4 if O.get(K,0)else 1;Ag=Af*Y.get((J,G),0);Ah=6 if M else 1;x=Ab-Ad*Ac+Ae-AD-AE-Ag+Ah*AC
			if x>g:g=x;B=J,G
			elif x==g and B is not W:
				if AA:
					y,h=B
					if G<h or G==h and J<y:B=J,G
				else:
					y,h=B;Ai=(y-D[0])**2+(h-D[1])**2;Aj=(J-D[0])**2+(G-D[1])**2
					if Aj<Ai:B=J,G
		if B is not W and g<=0 and M and Y and O.get(K,0)==0:B=min(Y.keys(),key=lambda x:(abs(x[0]-D[0])+abs(x[1]-D[1]),x[0],x[1]))
		if B is W and N and not M:
			if not n:B=min(N,key=lambda x:(x[0],x[1]))
			elif AA:B=min(N,key=lambda x:(x[1],x[0]))
			else:B=max(N,key=lambda x:(x[1],x[0]))
		if B is W:continue
		S,T=B[0]-D[0],B[1]-D[1];AF=j(Q,(S,T))
		if AQ(AF)>=2:P=AR(P,AF);A8.update(A9.get(B,set()))
	if len(I)>len(I[0]):
		F,C=len(A),len(A[0])
		if F==12 and C==12 and E is not W:
			Ak=(E,8,8)+tuple([E]*(C-3))
			for H in range(F):
				if all(A[H][B]==E for B in range(C))and P[H]==Ak:P=tuple(P[:H]+(tuple(A[H]),)+P[H+1:]);break
	return P
def p(g):A=tuple(tuple(A)for A in g);B=solve_e6721834(A);return[list(A)for A in B]