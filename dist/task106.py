B=zip
def p(j):A=lambda c:[*map(list,B(*c[::-1]))];return[c+y for(c,y)in B(j,A(j))]+[c+y for(c,y)in B(A(A(A(j))),A(A(j)))]