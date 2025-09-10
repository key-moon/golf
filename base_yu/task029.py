# best: 108(2F, biz) / others: 115(jailctf merger), 117(4atj sisyphus luke Seek mukundan), 118(xsot ovs att joking mewheni), 185(J&R), 185(jonas ryno kg583)
# ================================================== 108 ===================================================
# p=lambda g:[u for c in sum(g,[])if c not in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[])][0]
# lambda g:[u for c in sum(g,[])if~-(c in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[]))][0]
# lambda g,c=0:~-(c in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[]))and u or p(g,c+1)
p=lambda g,c=0:-~-(c in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[]))*u or p(g,c+1)

# def p(g):
#  for c in {*sum(g,[])}:
#   u=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1]
#   if c not in sum(u,[]):
#    return u







