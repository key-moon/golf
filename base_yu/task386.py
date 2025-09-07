# best: 52(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni, mukundan) / others: 55(biz), 56(natte), 56(duckyluuk), 56(jacekwl Potatoman), 56(HashPanda)
# ======================= 52 =======================
# p=lambda g:[[*eval("3-(s.pop(0)|s[3]and 3),"*3)]for s in g]
# p=lambda g:[[3-3*(s[i]|s[i+4]>0)for i in(0,1,2)]for s in g]
p=lambda g:[eval("3*(s.pop(0)|s[3]<1),"*3)for s in g]
