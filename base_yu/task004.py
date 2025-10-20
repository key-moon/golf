# best: 74(jailctf merger) / others: 80(Code Golf International), 80(4atj sisyphus luke Seek mukundan), 83(ox jam), 91(import itertools), 93(2F)
# ================================== 74 ==================================
# p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<sum(t)<3*c))]+s for s,t in zip(g,g[1:]+g)]
