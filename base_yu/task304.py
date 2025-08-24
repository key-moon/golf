# best: 92(biz, sisyphus) / others: 93(ovs), 93(mukundan), 101(Seek64), 101(duckyluuk), 101(cg)
# =========================================== 92 ===========================================
# p=lambda g:[[g[i//3][j//3]==max(u:=sum(g,[]),key=u.count)and g[i%3][j%3]for j in range(9)]for i in range(9)]
p=lambda g:[[(x==max(u:=sum(g,[]),key=u.count))*y for x in s for y in t]for s in g for t in g]

# p=lambda g,R=range(9):[[(g[i//3][j//3]==max(u:=sum(g,[]),key=u.count))*g[i%3][j%3]for j in R]for i in R]