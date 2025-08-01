def p(g):
 d={v:d.get(v,0)+1 for v in sum(g,[])if v}
 return [[k]for k in sorted(d,key=d.get,reverse=1)]