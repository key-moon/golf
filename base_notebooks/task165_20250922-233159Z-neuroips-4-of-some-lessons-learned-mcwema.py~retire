def p(j):
	from collections import Counter as Q,deque;G,M=len(j),len(j[0]);N=Q(sum(j,[])).most_common()[0][0];J=[[0]*M for A in range(G)];H=[]
	for A in range(G):
		for B in range(M):
			if J[A][B]or j[A][B]==N:continue
			R=j[A][B];O=deque([(A,B)]);J[A][B]=1;K=[(A,B)]
			while O:
				C,D=O.popleft()
				for(E,F)in[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
					if 0<=C+E<G and 0<=D+F<M and not J[C+E][D+F]and j[C+E][D+F]==R:J[C+E][D+F]=1;O.append((C+E,D+F));K.append((C+E,D+F))
			S,T=[A for(A,B)in K],[A for(B,A)in K];H.append((R,K,(min(S),min(T),max(S),max(T))))
	if not H:return j
	H.sort(key=lambda t:len(t[1]),reverse=1);I=H[0];P=H[1:]
	if not P:return j
	U=Q(A for(A,B,__)in P).most_common()[0][0];V={};[V.setdefault(A,[]).append(B)for(A,B)in I[1]];[A.sort()for A in V.values()];L={};[L.setdefault(D,[]).append(C)for(A,B,E)in P if A==U for(C,D)in B];[A.sort()for A in L.values()];W=[A for(A,B)in{A:[B for(B,C)in I[1]if C==A]for(B,A)in I[1]}.items()if A in L and L[A][-1]>=B[-1]and any(j[C][A]==N for C in range(B[0],G)if C not in B)];W and[j[B].__setitem__(A,U)for A in sorted(W)for B in range(min(B for(B,C)in I[1]if C==A),G)if B not in[B for(B,C)in I[1]if C==A]and j[B][A]==N];return j
