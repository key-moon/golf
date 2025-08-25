# best: 67(joking+MWI, joking/MWI, joking) / others: 69(ovs), 69(luke/sisyphus/Seek), 69(duckyluuk), 69(sisyphus), 72(biz)
# =============================== 67 ==============================
# p=lambda g:[([0,0,0],s[5:2:-1])[g[3][3]>0]+s[3:6]+([0,0,0],s[5:2:-1])[g[3][5]>0]for s in g[:3]]+g[3:]
p=lambda g:[(t:=(s[:3],s[5:2:-1]))[g[3][3]>0]+s[3:6]+t[g[3][5]>0]for s in g[:3]]+g[3:]
