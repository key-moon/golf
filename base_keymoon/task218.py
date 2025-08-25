# best: 60(luke) / others: 61(sisyphus), 67(joking+MWI), 72(Seek64), 72(joking), 74(mukundan)
# lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if any(r)and g!=r]
# 類題: 377
# =========================== 60 ===========================
p=lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if(g!=r)&any(r)]