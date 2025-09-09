# best: 179(4atj sisyphus luke Seek mukundan) / others: 188(xsot ovs att joking mewheni), 193(2F), 193(biz), 242(jailctf merger), 273(jonas ryno kg583)
# ====================================================================================== 179 ======================================================================================
# p=lambda g:(x:=max(((r-l)*(d-u),s)for d in range(len(g)+1)for u in range(d)for r in range(len(g[u])+1)for l in range(r)if (s:=[t[l:r]for t in g[u:d]])and min(s[-1]+s[0]+[min(t[0],t[-1])for t in s])>0)[1])and[[v and sum({*sum(x,[])})-t[0] for v in t]for t in x]
p=lambda g:[[v and sum({*sum(g,[])})-t[0] for v in t]for t in max((m,s)for(m,s)in(((r-l)*(d-u),[t[l:r]for t in g[u:d]])for d in range(len(g)+1)for u in range(d)for r in range(len(g[u])+1)for l in range(r))if 0<min(s[-1]+s[0]+[min(t[0],t[-1])for t in s]))[1]]


# def p(g):
#  _,x=max(((r-l)*(d-u),s)for d in range(len(g)+1)for r in range(len(g[0])+1)for l in range(r)for u in range(d)if (s:=[t[l:r]for t in g[u:d]])and 1==len({*s[-1],*s[0],*[min(v[0],v[-1])for v in s]})<=s[0][0])
#  return[[v and sum({*sum(x,[])})-t[0] for v in t]for t in x]


# def p(g):
#  t,j=range,len
#  x=m=0
#  for d in t(j(g)+1):
#   for r in t(j(g[0])+1):
#    for l in t(r):
#     for u in t(d):
#      s=[t[l:r]for t in g[u:d]]
#      b=s[-1]+s[0]+[min(v[0],v[-1])for v in s]
#      # m<(r-l)*(d-u) and len(set(b)) == 1 and 1 <= b[0]
#      if (m<(S:=(r-l)*(d-u)))==j({*b})<=b[0]:m,x=S,s
#  c,n=sum({*sum(x,[])})-x[0][0],j(x)
#  for i in t(m):x[i%n][i//n]=x[i%n][i//n]and c
#  return x




