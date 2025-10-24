# best: 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II) / others: 66(intgrah jimboko awu macaque sammyuri), 67(Code Golf International), 67(4atj sisyphus luke Seek mukundan), 67(import itertools), 67(jailctf merger)
# =========================== 59 ==========================
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
p=lambda g:(u:=[*zip(*[*zip(*g)]+g[::-1])])+[s[::-1] for s in u[::-1]]
# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]
