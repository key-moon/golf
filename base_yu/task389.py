# best: 57(4atj sisyphus luke Seek mukundan, biz, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 60(mukundan), 63(kg583), 63(jacekwl Potatoman), 63(jonas ryno kg583), 63(Yuchen20)
# ========================== 57 =========================
# p=lambda g:[[(v==5)*sum({*sum(g,[])}-{v})for v in s]for s in g]
p=lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
