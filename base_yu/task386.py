# best: 50(Code Golf International, lv1.dev, jailctf merger) / others: 52(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 52(4atj sisyphus luke Seek mukundan), 52(LogicLynx), 52(ALE-Agent), 52(FuunAgent)
# ====================== 50 ======================
# lambda g:[[*eval("3-(s.pop(0)|s[3]and 3),"*3)]for s in g]
# lambda g:[[3-3*(s[i]|s[i+4]>0)for i in(0,1,2)]for s in g]
# lambda g:[eval("3&~(s.pop(0)|s[3]*3),"*3)for s in g]
p=lambda g:[eval("3*(s.pop(0)|s[3]<1),"*3)for s in g]
