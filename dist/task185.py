B=range
A=zip
def p(g):
 c=max(g)[0]
 for _ in B(2):g=[*A(*[(l:=c)and[(v==l!=c)*(l:=v)for*t,v in A(*g,s)if all(t)+_]for s in g if all(s)+_])]
 for _ in B(40):g=[*A(*g[any(g[-1])-2::-1])]
 return g