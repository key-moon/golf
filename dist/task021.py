B=set
A=len
def p(g):s=next(r for r in g if A(B(r))==1)[0];C=sum(A(B(r))==1for r in g);D=sum(A(B(c))==1for c in zip(*g));d=next(x for r in g for x in r if x!=s);return[[d]*(D+1)]*(C+1)