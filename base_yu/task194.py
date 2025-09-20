# best: 67(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 74(ox jam), 74(xsot ovs att joking mewheni), 75(natte), 76(JRKX), 76(kabutack)
# =============================== 67 ==============================
# p=lambda g:(t:=[*zip(*g+[*zip(*g)][::-1])])and[s[::-1]for s in t]+t[::-1]
p=lambda g:(u:=[*zip(*[*zip(*g)]+g[::-1])])+[s[::-1] for s in u[::-1]]
# def p(g):
#  t=[*zip(*g+[*zip(*g)][::-1])]
#  return[s[::-1]for s in t]+t[::-1]
