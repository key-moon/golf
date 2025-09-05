# best: 73(luke, mukundan, 4atj, luke/sisyphus/Seek) / others: 74(joking+MWI), 74(joking/MWI), 74(joking), 75(natte), 75(sisyphus)
# ================================== 73 =================================
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
p=lambda g:(u:=[*zip(*[*zip(*g)]+g[::-1])])+[s[::-1] for s in u[::-1]]
# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]