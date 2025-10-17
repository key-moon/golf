# best: 52(jailctf merger, 4atj sisyphus luke Seek mukundan, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 54(natte), 54(cubbus), 54(jacekw Potatoman nauti natte), 55(2F), 55(biz)
# ======================= 52 =======================
# lambda g:[[*eval("3-(s.pop(0)|s[3]and 3),"*3)]for s in g]
# lambda g:[[3-3*(s[i]|s[i+4]>0)for i in(0,1,2)]for s in g]
# lambda g:[eval("3&~(s.pop(0)|s[3]*3),"*3)for s in g]
p=lambda g:[eval("3*(s.pop(0)|s[3]<1),"*3)for s in g]
