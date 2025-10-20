# best: 67(Code Golf International, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger) / others: 68(ox jam), 75(jacekw Potatoman nauti natte), 75(natte), 75(biz), 76(JRKX)
# =============================== 67 ==============================
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
p=lambda g:(u:=[*zip(*[*zip(*g)]+g[::-1])])+[s[::-1] for s in u[::-1]]
# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]
