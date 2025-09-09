# best: 64(xsot ovs att joking mewheni) / others: 65(4atj sisyphus luke Seek mukundan), 65(jailctf merger), 66(natte), 74(Yuchen20), 75(HETHAT)
# ============================= 64 =============================
# 345678901234567890123456789012345678901234567890123456789012345
# p=lambda g:(k:=                      )and[s[::-k]for s in g[::k]]
# p=lambda g:(k:=1+g[0].index([s[0]for s in g if {*s}=={s[0]}][0]))and[s[::-k]for s in g[::k]]
# p=lambda g:(k:=[i+1for i,s in enumerate(g)if{*s}=={s[0]}][0])and[s[::-k]for s in g[::k]]
# p=lambda g:(k:=[i+1for i in range(8)if g[0]!=g[i]][0])and[s[::-k]for s in g[::k]]
# p=lambda g:[[s[::-k]for s in g[::k]]for k in range(1,8)if g[0]!=g[k-1]][0]
# p=lambda g:[[s[::-k]for s in g[::k]]for k in(3,4,5,6)if g[0]!=g[k-1]][0]
p=lambda g:[[s[::-k]for s in g[::k]]for k in b""if g[0]!=g[k-1]][0]

# p=lambda g:[[y for x,y in zip([10]+t,t)if x!=y][::-2]for s,t in zip([0]+g,g)if s!=t][::2]


# p=lambda g:(k:=[i+1for i,v in enumerate(g[0])if v!=g[0][0]][0])and[s[::-k]for s in g[::k]]

#  8 2 3if
# 11 2 4
# 11 3 3
# 15 3 4
# 14 4 3
# 19 4 4
# 17 5 3
# 23 5 4



