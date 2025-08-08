A=zip
def p(g):r=lambda x:[*map(list,A(*x[::-1]))];return[x+y for(x,y)in A(g,r(g))]+[x+y for(x,y)in A(r(r(r(g))),r(r(g)))]