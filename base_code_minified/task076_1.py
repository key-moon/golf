def p(A):
	J,K=len(A),len(A[0]);H=[]
	for C in range(J):
		for D in range(K):
			if A[C][D]==4:
				if D==0 or A[C][D-1]!=4:
					B=1
					while D+B<K and A[C][D+B]==4:B+=1
					if B>1:H.append((C,D,0,1,B))
				if C==0 or A[C-1][D]!=4:
					B=1
					while C+B<J and A[C+B][D]==4:B+=1
					if B>1:H.append((C,D,1,0,B))
	for L in range(len(H)):
		for V in range(L+1,len(H)):
			W,X,E,F,M=H[L];N,O,Y,Z,a=H[V]
			if E==Y and F==Z and M==a:
				for P in range(J):
					for Q in range(K):
						I=A[P][Q]
						if I and I!=4:
							R,S=P-W,Q-X;G=R*E+S*F
							if 0<=G<M:
								T,U=R-G*E,S-G*F
								if(T,U)==(F,-E):A[N+G*E-F][O+G*F+E]=I
								if(T,U)==(-F,E):A[N+G*E+F][O+G*F-E]=I
				return A
	return A