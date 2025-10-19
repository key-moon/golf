# best: 58(JRKKX, jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, kdmitrie, import itertools) / others: 61(MKRC), 61(ShadowPrompt Labs), 61(kabutack), 61(Tony Li), 61(jonas ryno kg583)
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
# lambda g:eval(str(g+g[(g[2]!=g[5])*2:][:3]).replace(*"12"))
p=lambda g:[[c*2for c in r]for r in g+g[(g[2]!=g[5])*2:][:3]]

#  g+g[(g[2]!=g[5])*2:][:3]
# [g[:3],g[2:5]][g[:3]*2!=g]
# [a:=g[:3],g[2:5]][a*2!=g]
