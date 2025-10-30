# best: 86(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 89(HIMAGINE THE FUTURE.), 112(intgrah jimboko awu macaque sammyuri), 115(HETHAT), 123(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 124(MasukenSamba)
# ======================================== 86 ========================================
# p=lambda g,c=-1:c*g or p([(u:={0})and[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
p=lambda g,c=-1,u={0}:c*g or p([[sum(u|(u:=u^{*s}&{*t}))for t in g]for s in zip(*g)],c+1)
