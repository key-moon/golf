def j(g):return list(zip(*g[::-1]))
def p(g,u=len,r=range):
 m=0
 if max(g[0].count(l)for l in r(10))-1<u(g[0])/2:m=1;g=j(g)
 k,i=u(g),u(g[0])
 for x in r(k):t=sorted([[g[x].count(l),l]for l in r(10)])[-1][1];g[x]=[t]*i
 if m:g=j(j(j((g))))
 return g