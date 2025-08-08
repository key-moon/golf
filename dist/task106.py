A=zip
def p(g):r=lambda m:[*map(list,A(*m[::-1]))];a=r(g);b=r(a);c=r(b);return[x+y for(x,y)in A(g,a)]+[x+y for(x,y)in A(c,b)]