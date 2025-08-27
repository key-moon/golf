# best: 66(luke, 4atj sisyphus luke Seek) / others: 68(mukundan), 71(joking MeWhenI), 71(kabutack), 71(MeWhenI), 83(joking)
# ============================== 66 ==============================
# lambda g:([(r[1:3+(r[0]==r[3])][:3]*9)[:len(g)]for r in g[:2]]*99)[:len(g)]
# lambda g:([(r[1:3+(r[0]==r[3])]*9)[:(a:=len(g))]for r in g[:2]]*99)[:a]
p=lambda g:[(r[1:3+(r[0]==r[3])]*9)[:len(g)]for r,_ in zip(g[:2]*99,g)]
