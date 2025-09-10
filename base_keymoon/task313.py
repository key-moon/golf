# best: 63(jailctf merger) / others: 64(4atj sisyphus luke Seek mukundan), 65(xsot ovs att joking mewheni), 71(kabutack), 71(intgrah jimboko awu macaque sammyuri), 81(natte)
# ============================= 63 ============================
# lambda g:([(r[1:3+(r[0]==r[3])][:3]*9)[:len(g)]for r in g[:2]]*99)[:len(g)]
# lambda g:([(r[1:3+(r[0]==r[3])]*9)[:(a:=len(g))]for r in g[:2]]*99)[:a]
p=lambda g:[(r[1:3+(r[0]==r[3])]*9)[:len(g)]for r,_ in zip(g[:2]*99,g)]











