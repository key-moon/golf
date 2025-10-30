# best: 50(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger, ox jam, biz) / others: 53(HIMAGINE THE FUTURE.), 54(jacekw Potatoman nauti natte), 54(ShadowPrompt Labs), 54(HETHAT), 54(natte)
# p=lambda g:[[6*any(s)for s in zip(*zip(*[iter(r)]*3))]for r in g]
# p=lambda g:[[6*(0<sum(s))for s in zip(r,r[3:])]for r in g]
# p=lambda g:[[6*(0<a+b)for a,b in zip(r,r[3:])]for r in g]
# p=lambda g:[[6*(0<r[i]+r[i+3])for i in(0,1,2)]for r in g]
# p=lambda g:[[6*any(r[i::3])for i in(0,1,2)]for r in g]
# p=lambda g:[[6*any(s)for s in zip(r,r[3:])]for r in g]
# in range(3)
# in(0,1,2)
# in b"012"
# 3,4 -> 6
# lambda g:[[               for s in r]for r in g]
# lambda g:[[          for i in(0,1,2)]for r in g]
# lambda g:[[    for s in zip(r,r[3:])]for r in g]
# ====================== 50 ======================
p=lambda g:[[6*any(r[i::3])for i in(0,1,2)]for r in g]
