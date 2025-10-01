def T(V,R):C=list(zip(*V));A=int((min(C[1])+max(C[1]))/2);B=int((min(C[2])+max(C[2]))/2);V=list(zip(*[((C,-E+B+A,D-A+B),(C,E-B+A,-D+A+B))if R else((C,2*A-D,E),(C,D,2*B-E))for(C,D,E)in V]));return V
def p(d):
	E=range;Q=len;F=[];K=[];G=Q(d);H=Q(d[0]);R=[];L=list.extend
	for A in E(G):
		for D in E(H):
			if(C:=d[A][D])and(C,A,D)not in F+K:
				B=[(C,A,D)];I=set()
				while B:
					J=B.pop(0)
					if J not in I:I.add(J);L(B,[(C,S,U)for(A,B)in[(0,-1),(0,1),(1,0),(-1,0)]if 0<=(S:=J[1]+A)<G if 0<=(U:=J[2]+B)<H if(C:=d[S][U])])
				M=list(I)
				if len(I)>3:R.append(M);F;L(F,M)
				else:L(K,M)
	for B in R:
		for A in E(-G,G):
			for D in E(-H,H):
				N=[(B[0],B[1]+A,B[2]+D)for B in B];O=T(N,1);P=T(N,0);W=T(O[0],0)+T(O[1],0);X=T(P[0],1)+T(P[1],1);Y=[N]+O+P+W+X;V=[A for A in Y if len([A for A in A if A not in F and A in K])==3]
				if V:
					for(A,(Z,a,C))in enumerate(V[0]):d[a][C]=Z;d[B[A][1]][B[A][2]]=0
	return d