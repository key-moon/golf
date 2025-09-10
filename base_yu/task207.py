# best: 81(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 84(2F), 84(kabutack), 84(biz), 86(cg), 86(Yuchen20)
# ====================================== 81 =====================================
# p=lambda g:[[sum(u:=[*s[j::3],*t[j::3]])%(max(*u,1)*3)for j in(0,1)]for s,t in zip(g,g[3:])]
# p=lambda g:[[sum([*g[i][j::3],*g[i+3][j::3]])%(max(map(max,g))*3)for j in(0,1)]for i in(0,1)]
# p=lambda g:[[sum([*g[i][j::3],*g[i+3][j::3]])%(max([*g[0],*g[1]])*3)for j in(0,1)]for i in(0,1)]
# p=lambda g:[[sum([*s[j::3],*t[j::3]])%(max([*s,*t])*3)for j in(0,1)]for s,t in zip(g,g[3:])]
p=lambda g:[[sum(u:=g[i][j::3]+g[i+3][j::3])%(max(*u,1)*3)for j in(0,1)]for i in(0,1)]

# 0 -> 0
# 1 -> 1
# 2 -> x
# 3 -> 0
# 4 -> 1







