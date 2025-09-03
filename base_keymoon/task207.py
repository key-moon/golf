# best: 81(4atj sisyphus luke Seek) / others: 84(Seek64), 84(biz), 84(luke), 84(4atj), 84(kabutack)
# lambda g:[[(a:=sorted(g[i][j::3]+g[i+3][j::3]))[0]^a[1]^a[3]for j in(0,1)]for i in(0,1)]
# ====================================== 81 =====================================
# lambda g:[eval("[sum(u:=g.pop(0)[j::3]+g[2][j::3])%(9**max(u))for j in(0,1)],"*3)] <- g is not defined
# lambda g:[[sum(u:=g[i][j::3]+g[i+3][j::3])%(max(*u,1)*3)for j in(0,1)]for i in(0,1)]
p=lambda g:min(p:=[[r[j:j+2]for r in g[i:i+2]]for i in(0,3)for j in(0,3)],key=p.count)
