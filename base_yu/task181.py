# best: 67(jacekw Potatoman nauti natte, import itertools, jailctf merger, ox jam) / others: 69(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 69(Code Golf International), 69(4atj sisyphus luke Seek mukundan), 69(MasukenSamba), 69(HIMAGINE THE FUTURE.)
# =============================== 67 ==============================
# p=lambda g:[([0,0,0],s[5:2:-1])[g[3][3]>0]+s[3:6]+([0,0,0],s[5:2:-1])[g[3][5]>0]for s in g[:3]]+g[3:]
# p=lambda g:[(t:=(s[:3],s[5:2:-1]))[g[3][3]>0]+s[3:6]+t[g[3][5]>0]for s in g[:3]]+g[3:]

def p(g):
 for s in g[:3]:
  A=g[3][5]*3//2
  s[A:A+3]=s[5:2:-1]
 return g


# p=lambda g:exec("for s in g[:3]:A=g[3][5]*3//2;s[A:A+3]=s[5:2:-1]")or g
