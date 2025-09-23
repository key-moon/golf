# best: 52(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 54(cubbus), 55(2F), 55(biz), 56(natte), 56(duckyluuk)
# ======================= 52 =======================
# lambda g:[[*eval("3-(s.pop(0)|s[3]and 3),"*3)]for s in g]
# lambda g:[[3-3*(s[i]|s[i+4]>0)for i in(0,1,2)]for s in g]
# lambda g:[eval("3&~(s.pop(0)|s[3]*3),"*3)for s in g]
p=lambda g:[eval("3*(s.pop(0)|s[3]<1),"*3)for s in g]
