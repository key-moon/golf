# best: 49(Code Golf International, lv1.dev, jailctf merger, ox jam) / others: 56(HIMAGINE THE FUTURE.), 57(4atj sisyphus luke Seek mukundan), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 59(LogicLynx), 59(MasukenSamba)
# ====================== 49 =====================
# 345678901234567890123456789012345678901234567890123456
def p(g):
 for s,t in zip(g,g[1:]):
  if s==t:
   t[1-t.index(max(t))%2::2]=g[0][::2]
 return g
