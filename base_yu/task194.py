# best: 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, jailctf merger) / others: 67(Code Golf International), 67(4atj sisyphus luke Seek mukundan), 67(import itertools), 68(ox jam), 69(HIMAGINE THE FUTURE.)
# =========================== 59 ==========================
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
p=lambda g:(u:=[*zip(*[*zip(*g)]+g[::-1])])+[s[::-1] for s in u[::-1]]
# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]
