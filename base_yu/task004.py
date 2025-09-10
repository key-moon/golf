# best: 80(4atj sisyphus luke Seek mukundan) / others: 81(jailctf merger), 83(xsot ovs att joking mewheni), 93(2F), 93(biz), 108(jacekwl Potatoman nauti)
# ===================================== 80 =====================================
# p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<sum(t)<3*c))]+s for s,t in zip(g,g[1:]+g)]








