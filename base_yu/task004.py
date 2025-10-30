# best: 73(ox jam) / others: 74(jailctf merger), 80(Code Golf International), 80(4atj sisyphus luke Seek mukundan), 84(HIMAGINE THE FUTURE.), 91(import itertools)
# ================================== 73 =================================
# p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<sum(t)<3*c))]+s for s,t in zip(g,g[1:]+g)]
