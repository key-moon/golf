# best: 77(ovs, luke, mukundan, 4atj, luke/sisyphus/Seek) / others: 79(Bulmenisaurus), 79(joking+MWI), 79(joking/MWI), 79(att), 79(kabutack)
# ==================================== 77 ===================================
p=lambda g,R=range(17):[[g[i][j]or(g[i%6][j%6]>0)*g[0][5]for j in R]for i in R]
# p=lambda g:[[v or(w>0)*g[0][5]for v,w in zip(s,t[:6]*3)]for s,t in zip(g,g[:6]*3)]
