# best: 65(ovs, luke, mukundan, luke/sisyphus/Seek, Seek64, nauti, joking+MWI, joking/MWI, HashPanda, sisyphus) / others: 66(dbdr), 66(kabutack), 66(biz), 67(joking), 74(Ali)
# ============================== 65 =============================
# p=lambda g:(u:=[*zip(*g)])and[[0,*g[0],0],*[*zip(*(u[:1]+u+u[-1:]))],[0,*g[-1],0]]
p=lambda g:[[0,*g[0],0],*[s[:1]+s+s[-1:]for s in g],[0,*g[-1],0]]