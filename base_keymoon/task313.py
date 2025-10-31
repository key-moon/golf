# best: 61(Code Golf International) / others: 62(ox jam), 63(jailctf merger), 64(4atj sisyphus luke Seek mukundan), 64(LogicLynx), 64(FuunAgent)
# ============================ 61 ===========================
# lambda g:([(r[1:3+(r[0]==r[3])][:3]*9)[:len(g)]for r in g[:2]]*99)[:len(g)]
# lambda g:([(r[1:3+(r[0]==r[3])]*9)[:(a:=len(g))]for r in g[:2]]*99)[:a]
p=lambda g:[(r[1:3+(r[0]==r[3])]*9)[:len(g)]for r,_ in zip(g[:2]*99,g)]
