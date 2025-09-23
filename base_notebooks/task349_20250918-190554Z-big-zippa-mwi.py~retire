def solve_db93a21d(I):
	A=[A[:]for A in I];B,D=len(A),len(A[0]);from collections import Counter as a,deque;T=a([B for A in A for B in A]).most_common(1)[0][0];M=[[False]*D for A in range(B)];U=[]
	for E in range(B):
		for C in range(D):
			if M[E][C]:continue
			M[E][C]=True;J=A[E][C]
			if J==T:continue
			S=deque([(E,C)]);F=[(E,C)]
			while S:
				K,L=S.popleft()
				for V in(-1,0,1):
					for W in(-1,0,1):
						if V==0 and W==0:continue
						G,H=K+V,L+W
						if 0<=G<B and 0<=H<D and not M[G][H]and A[G][H]==J:M[G][H]=True;S.append((G,H));F.append((G,H))
			U.append((J,F))
	for E in range(B):
		for C in range(D):
			if A[E][C]==9:
				for X in range(E,B):
					if A[X][C]==T:A[X][C]=1
	for(J,F)in U:
		if J!=9 or not F:continue
		b=min(A for(A,B)in F);c=max(A for(A,B)in F);Y=min(A for(B,A)in F);Z=max(A for(B,A)in F);d=(Z-Y+1)//2
		for N in range(1,d+1):
			O,P=b-N,c+N;Q,R=Y-N,Z+N
			if 0<=O<B:
				for L in range(max(0,Q),min(D,R+1)):A[O][L]=3
			if 0<=P<B:
				for L in range(max(0,Q),min(D,R+1)):A[P][L]=3
			if 0<=Q<D:
				for K in range(max(0,O),min(B,P+1)):A[K][Q]=3
			if 0<=R<D:
				for K in range(max(0,O),min(B,P+1)):A[K][R]=3
	return A
def p(g):return solve_db93a21d([A[:]for A in g])