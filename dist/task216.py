A=range
p=lambda g:max((all(y:=sum(x:=[s[l:t%21]for s in g[u:t//21]],[])),y.count(2),len(y),x)for t in A(441)for l in A(t%21)for u in A(t//21))[3]