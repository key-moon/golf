A=enumerate
def p(g):return[[2if not(z:=[(y,x)for(y,r)in A(g)for(x,v)in A(r[j:j+4])if v==0])else 3if max(x for(_,x)in z)-min(x for(_,x)in z)>1else 8if min(y for(y,_)in z)<2else 4]*3for j in(0,5,10)]