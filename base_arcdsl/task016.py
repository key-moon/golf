def P(A,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in A)
def p(I):I=tuple(map(tuple,I));A=P(I,3,4);B=P(A,8,9);C=P(B,2,6);D=P(C,1,5);return[*map(list,D)]