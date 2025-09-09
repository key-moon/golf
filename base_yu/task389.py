# best: 57(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, biz, jailctf merger, xsot ovs att joking mewheni) / others: 60(mukundan), 61(intgrah jimboko awu macaque sammyuri), 63(jacekwl Potatoman), 63(MasukenSamba), 63(kabutack)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
