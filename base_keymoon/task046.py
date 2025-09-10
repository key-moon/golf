# best: 170(xsot ovs att joking mewheni) / others: 178(4atj sisyphus luke Seek mukundan), 196(natte), 217(duckyluuk), 225(jailctf merger), 263(Afordancja)
# ================================================================================= 170 ==================================================================================
# f p(g):a=[*zip(*g)];o=2;return[*zip(*[[[v,sum({*S,*s,*t}-{5})][v==5]for v in([0,0,*s]*2)[o:o+3]]for s,S,t in zip(a,[[]]+a,a[1:]+[[5]])if any(s)or(o:=t.index(5)+o-[*S,5].index(5))*0])]
# f p(g):a=[*zip(*g)];o=2;return[*zip(*[[[v,u][v==5]for v in[0,0,*s,0,0][o:o+3]]for s,S,t in zip(a,[()]+a,a[1:]+[(5,)])if any(s)and(u:=sum({*S+s+t}-{5}))or(o:=t.index(5)+o-[*S,5].index(5))*0])]
def p(g):a=[*zip(*g)];o=2;return[*zip(*[[[v,sum({*S+s,*t}-{5})][v==5]for v in[0,0,*s,0,0][o:o+3]]for s,S,t in zip(a,[()]+a,a[1:]+[[5]])if any(s)or(o:=t.index(5)+o-[*S,5].index(5))*0])]

# 棒みたいなのないかと思ったがある 無念

# o: 列の開始位置とする(暫定)
# [0,0,*s,0,0][o:o+3]
# 
# 0:
# next: 5,0,0 (次の5)
# prev: 0,0,5 (合わせるべき位置)
# 1:
# next: 0,5,0 | 5,0,0
# prev: 0,0,5 | 0,5,0

# [5, 2, 0], [0, 5, 0] -> 

# ブロックの終わり際に次のために終わりの場所を考える 一旦終わりの位置(=遷移先)を保存しておく
# 終わりの位置は
# 次の o は next-prev+2?
# 0: 0-2+1
# 1: 1









