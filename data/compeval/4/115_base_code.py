def p(g):
    t=len({*g[0]})>1
    a=g[0]if t else[i[0]for i in g]
    o=[];v=None
    for c in a:
        if c!=v:o+=[c];v=c
    return t and[o]or[[x]for x in o]
