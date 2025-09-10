# best: 58(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 61(kdmitrie), 61(KN), 61(jacekw), 61(Ali), 61(kabutack)
# ========================== 58 ==========================
# サイクルを発見する（3サイクルか4サイクルかの二択）
# [c*2for c in r]
# map(lambda x:x*2,r)
# def p(g):
#   if g[:3]==g[3:]:
#     return[[c*2for c in r]for r in g+g[:3]]
#   else:
#     return[[c*2for c in r]for r in g+g[2:5]]
# lambda g:[[c*2for c in r]for r in g+g[(g[:3]*2!=g)*2:][:3]]
p=lambda g:[[c*2for c in r]for r in g+g[(g[2]!=g[5])*2:][:3]]

#  g+g[(g[2]!=g[5])*2:][:3]
# [g[:3],g[2:5]][g[:3]*2!=g]
# [a:=g[:3],g[2:5]][a*2!=g]











