# best: 67(jailctf merger, xsot ovs att joking mewheni) / others: 69(duckyluuk), 69(4atj sisyphus luke Seek mukundan), 69(MasukenSamba), 69(intgrah jimboko awu macaque sammyuri), 72(2F)
# =============================== 67 ==============================
# p=lambda g:[([0,0,0],s[5:2:-1])[g[3][3]>0]+s[3:6]+([0,0,0],s[5:2:-1])[g[3][5]>0]for s in g[:3]]+g[3:]
# p=lambda g:[(t:=(s[:3],s[5:2:-1]))[g[3][3]>0]+s[3:6]+t[g[3][5]>0]for s in g[:3]]+g[3:]

def p(g):
 for s in g[:3]:
  A=g[3][5]*3//2
  s[A:A+3]=s[5:2:-1]
 return g


# p=lambda g:exec("for s in g[:3]:A=g[3][5]*3//2;s[A:A+3]=s[5:2:-1]")or g









