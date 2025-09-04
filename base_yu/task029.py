# best: 115(jailctf merger) / others: 117(4atj sisyphus luke Seek), 118(xsot ovs att joking mewheni), 129(mukundan), 195(Jonas), 201(nauti)
# ====================================================== 115 ======================================================
# p=lambda g:[u for c in sum(g,[])if c not in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[])][0]
p=lambda g:[u for c in sum(g,[])if~-(c in sum(u:=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1],[]))][0]

# def p(g):
#  for c in {*sum(g,[])}:
#   u=[[v for*t,v in zip(*g,s)if c in t][1:-1]for s in g if c in s][1:-1]
#   if c not in sum(u,[]):
#    return u
