A=zip
def p(g):a=[*map(list,A(*g[::-1]))];b=[*map(list,A(*g))][::-1];c=[i[::-1]for i in g[::-1]];return[x+y for(x,y)in A(g,a)]+[x+y for(x,y)in A(b,c)]