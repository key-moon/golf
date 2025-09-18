# best: 86(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 115(HETHAT), 166(Yuchen20), 175(MasukenSamba), 186(intgrah jimboko awu macaque sammyuri), 190(jonas ryno kg583)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([(u:={0})and[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
p=lambda g,c=-1,u={0}:c*g or p([[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
