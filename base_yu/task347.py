# best: 50(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 54(duckyluuk), 54(intgrah jimboko awu macaque sammyuri), 54(HETHAT), 56(kabutack), 56(jonas ryno kg583)
# ====================== 50 ======================
# p=lambda g:[[s[i]|s[i+3]and 6for i in range(3)]for s in g]
# p=lambda g:[[x|y and 6for x,y in zip(s,s[3:])]for s in g]
# p=lambda g:[[(x|y>0)*6for x,y in zip(s,s[3:])]for s in g]
p=lambda g:[eval("6*(s.pop(0)+s[2]>0),"*3)for s in g]




