f=lambda b:list(zip(*b[::-1]))
def p(b,i=len,a=range):
	o=[A[:]for A in b]
	for B in a(4):
		b=f(b);o=[list(A)for A in f(o)];F,g=i(b),i(b[0]);A=[(A,B)for A in a(F)for B in a(g)if b[A][B]==1]
		if A:
			G,H,I,J=min(A for(A,B)in A),max(A for(A,B)in A),min(A for(B,A)in A),max(A for(B,A)in A)
			for B in a(F-1):
				for A in a(g-2):
					E=[A for A in a(g)if o[B][A]>0]
					if E and i(E)>3:
						if b[B][A]==1 and b[B][A+2]==1:o[B][A+1]=2
						if min(E)<A+1<max(E)and b[B][A+1]==0:o[B][A+1]=2
				if B==G or B==H:
					for A in a(I,J+1):o[B][A]=2
					for B in a(G,H+1):o[B][A]=2
	for B in a(F):
		for A in a(g):
			if b[B][A]>0:o[B][A]=1
	return o