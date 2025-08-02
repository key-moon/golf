def p(A):
	for(D,I)in enumerate(A):
		for(E,F)in enumerate(I):
			if F==3:B,C=D,E
			if F==4:G,H=D,E
	J=(G>B)-(G<B);K=(H>C)-(H<C);A[B][C]=0;A[B+J][C+K]=3;return A