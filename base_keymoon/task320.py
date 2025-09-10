# best: 68(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 70(kabutack), 72(xsot ovs att joking mewheni), 76(MasukenSamba), 80(intgrah jimboko awu macaque sammyuri), 81(2F)
# 多分70までは縮むはず
# lambda g:[*zip(*[[s,s[:-(s.count(2)//2)]+99*(8,)][any(s)]for s in zip(*g)])] <- zipのclipを利用しようとした残骸
# lambda g:[*zip(*[s[:len(s)-(u:=s.count(2)//2)]+u*(8,)for s in zip(*g)])]
# =============================== 68 ===============================
p=lambda g:[*zip(*[s[:-(u:=s.count(2)//2)or 99]+u*(8,)for s in zip(*g)])]











