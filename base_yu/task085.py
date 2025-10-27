# best: 50(jailctf merger) / others: 56(HIMAGINE THE FUTURE.), 56(ox jam), 57(Code Golf International), 57(4atj sisyphus luke Seek mukundan), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ====================== 50 ======================
# 345678901234567890123456789012345678901234567890123456
def p(g):
 for s,t in zip(g,g[1:]):
  if s==t:
   t[1-t.index(max(t))%2::2]=g[0][::2]
 return g
