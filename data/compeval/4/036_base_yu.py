# best: 103(4atj sisyphus luke Seek) / others: 106(joking), 106(joking MeWhenI), 110(sisyphus), 113(4atj), 115(ovs)
# ================================================ 103 ================================================
# f=lambda g,d,c=-1:c*g or f([[*s]for s in zip(*g)if d in s],d,c+1)
# f=lambda g,d:[[v for*t,v in zip(*g,s) if d in t]for s in g if d in s]
# p=lambda g:min((s:=f(g,i))and(sum(t.count(0)for t in s),s)for i in sum(g,[]))[1]
# p=lambda g:min((s:=[[v for*t,v in zip(*g,s)if i in t]for s in g if i in s])and(sum(t.count(0)for t in s),s)for i in sum(g,[]))[1]
# p=lambda g:min((k:=1,s:=[[v for*t,v in zip(*g,s)if i in t if(k:=k+(v<1))]for s in g if i in s])and(k,s)for i in sum(g,g))[1]
p=lambda g:min((k:=1,[[v for*t,v in zip(*g,s)if i in t if(k:=k+(v<1))]for s in g if i in s],k)[::-1]for i in sum(g,[]))[1]
