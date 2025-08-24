# best: 47(luke, 4atj, att, sisyphus) / others: 48(kg583), 48(mukundan), 48(cg), 48(Seek64), 48(HashPanda)
# lambda g:[[max(s:=sum(g,[]),key=s.count)]*3]*3
# ===================== 47 ====================
p=lambda g:[[max(s:=sum(g,g),key=s.count)]*3]*3
