# best: 49(att, sisyphus) / others: 56(4atj), 58(joking+MWI), 59(HETHAT), 59(Seek64), 60(joking)
# ====================== 49 =====================
# p=lambda g:[r*2for r in zip(*filter(max,zip(*g)))if max(r)]
# p=lambda g,F=filter:[r*2for r in F(max,zip(*F(max,zip(*g))))]
# p=lambda g,c=2:c and p([*filter(max,zip(*g))]*c,c-1)or g
# p=lambda g,F=filter:[*F(max,zip(*[*F(max,zip(*g))]*2))]
p=lambda g,F=lambda c:[*filter(max,zip(*c))]:F(F(g)*2)
