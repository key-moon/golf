# best: 81(4atj sisyphus luke Seek, jailctf merger) / others: 82(mukundan), 86(kg583), 86(kabutack), 87(xsot ovs att joking mewheni), 91(Bulmenisaurus)
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
# ====================================== 81 =====================================
# lambda g:[R for r in g if(R:=[v for v in r if v==min(u:=[0]*99+sum(g,[]),key=u.count)])]
# lambda g:[R for r in g if(R:=r.count(v:=min(u:=[0]*99+sum(g,[]),key=u.count))*[v])]
p=lambda g:[c*[v]for r in g if(c:=r.count(v:=min(u:=sum(g,[0]*99),key=u.count)))]
