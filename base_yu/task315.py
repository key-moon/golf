# best: 63(luke, sisyphus) / others: 64(ovs), 64(mukundan), 64(att), 64(kabutack), 64(duckyluuk)
# ============================= 63 ============================
# p=lambda g,R=range(9):[[(g[i//3][j//3]>1)*g[i%3][j%3]for j in R]for i in R]
# p=lambda g:[sum([[[0,0,0],s][v>1]for v in t],[])for t in g for s in g]
p=lambda g:[[y*(x>1)for x in t for y in s]for t in g for s in g]

