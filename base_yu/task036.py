# best: 75(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, biz) / others: 84(2F), 90(ox jam), 95(HIMAGINE THE FUTURE.), 96(jacekw Potatoman nauti natte), 96(jacekw Potatoman nauti)
# =================================== 75 ==================================
# f=lambda g,d,c=-1:c*g or f([[*s]for s in zip(*g)if d in s],d,c+1)
# f=lambda g,d:[[v for*t,v in zip(*g,s) if d in t]for s in g if d in s]
# p=lambda g:min((s:=f(g,i))and(sum(t.count(0)for t in s),s)for i in sum(g,[]))[1]
# p=lambda g:min((s:=[[v for*t,v in zip(*g,s)if i in t]for s in g if i in s])and(sum(t.count(0)for t in s),s)for i in sum(g,[]))[1]
# p=lambda g:min((k:=1,s:=[[v for*t,v in zip(*g,s)if i in t if(k:=k+(v<1))]for s in g if i in s])and(k,s)for i in sum(g,g))[1]
# p=lambda g:min((k:=1,[[v for*t,v in zip(*g,s)if i in t if(k:=k+(v<1))]for s in g if i in s],k)[::-1]for i in sum(g,[]))[1]
# lambda g,c=1:(a:=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s])*(1<len(a)<6)or p(g,c+1)
# lambda g,c=0:DUMP((c%3-1)*g or(a:=[s for s in zip(*p(g,c+1))if c//3in s])*(1<len(a)<6)or p(g,c+1))
p=lambda g,c=1,d=1:-c*g or(a:=[s for s in zip(*p(g,c-1,d))if d in s])*(1<len(a)<6)or p(g,1,d+1)
