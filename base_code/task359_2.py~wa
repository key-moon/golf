def p(g):
  val_h,len_=len, # alias
  val_h=val_h(g);val_w=val_h(g[0])
  val_rn=sum(val_w-max(r.count(x)for x in r)for r in g)
  val_cn=sum(val_h-max(c.count(x)for x in c)for c in zip(*g))
  return [max(c,key=c.count)for c in zip(*g)]*val_h\
    if val_cn<val_rn\
    else [[max(r,key=r.count)]*val_w for r in g]
