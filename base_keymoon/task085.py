# best: 49(Code Golf International, lv1.dev, jailctf merger, ox jam) / others: 56(HIMAGINE THE FUTURE.), 57(4atj sisyphus luke Seek mukundan), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 59(LogicLynx), 59(MasukenSamba)
# 94
# lambda g,s=[]:[[1for r[~r.index(max(r))&1::2] in [len(r)//2*[0]]]for r in g if s==(s:=r)]and g
# 92
# def p(g,s=[]):
#  for r in g:
#   if r==s:r[~r.index(max(r))&1::2]=len(r)//2*[0]
#   s=r
#  return g
# 66
# lambda g,b=0:[g:=[r,[b:=[0,c][b==0]for c in r]][g==r]for r in g]
# lambda g,b=0:[g:=[r,[b:=c*(b<1)for c in r]][g==r]for r in g]
# lambda g,b=0:[g:=[[c,b:=c*(b<1)][g==r]for c in r]for r in g]
# ====================== 49 =====================
p=lambda g:[g:=[b:=c*(g!=r or b<1)for c in r]for r in g]
