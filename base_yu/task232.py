# best: 58(jailctf merger, ox jam) / others: 60(JRKX), 61(jonas ryno kg583 kabutack), 61(JRK), 61(4atj sisyphus luke Seek mukundan), 61(jonas ryno kg583)
# ========================== 58 ==========================
p=lambda g:[([0]*[*s,1].index(v:=max(*s,1))+[v,5]*9)[:len(s)]for s in g]
# p=lambda g:[(c:=0)or[(c:=v+(c and[5,max(s)][c==5]))for v in s]for s in g]

# 00 0
# 0v v
# v0 5
# 50 v
