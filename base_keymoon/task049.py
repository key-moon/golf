# p=lambda g:eval(min([str(a) for i in range(10) if 1==len(set(a:=[[c for c in r if c==i]for r in g if i in r]))],key=len))
# p=lambda g:eval(min([str([[i]*r.count(i)for r in g if i in r])for i in range(1,10) if str(i)in str(g)],key=len))
# p=lambda g:eval(min([str([[i]*r.count(i)for r in g if i in r]or"1,"*999)for i in range(1,10)],key=len))
# p=lambda g:eval(min([str([a for r in g if(a:=[i]*r.count(i))]or"1,"*999)for i in range(1,10)],key=len)) ←0だと破滅
# p=lambda g:min([[a for r in g if(a:=[i]*r.count(i))]or"1"*999for i in range(1,10)],key=len) ←いけるかと思ったんだけど駄目だった
# p=lambda g:eval(min([str([a for r in g if(a:=[i]*r.count(i))])for i in sum(g,[])if i],key=len)): 95
# [a for a in[[i]*r.count(i)for r in g]if a]
# [*filter(len,[[i]*r.count(i)for r in g])]
# [a for r in g if(a:=[i]*r.count(i))]
# sum(g,[])
# range(1,10)
# [i]*r.count(i)
# [i for c in r if i==c]
# =============================== best: 81 by 4atj ==============================
p=lambda g:eval(min([str([a for r in g if(a:=[i]*r.count(i))])for(i)in sum(g,[])if i],key=len))
