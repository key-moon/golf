# best: 65(luke, 4atj, luke/sisyphus/Seek, Seek64, natte, att) / others: 66(sisyphus), 71(nauti), 71(joking+MWI), 71(joking/MWI), 72(kabutack)
# ============================== 65 =============================
# p=lambda g,c=-1:c*g or p([s for s in zip(*g) if any(s)],c+1)[:3]
p=lambda g,c=-1:c*g or[*zip(*p([s for s in zip(*g)if any(s)],c+1))][:3]