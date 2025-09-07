# best: 80(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek) / others: 82(jailctf merger), 83(mukundan), 85(xsot ovs att joking mewheni), 93(biz), 139(duckyluuk)
# ===================================== 80 =====================================
# p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<sum(t)<3*c))]+s for s,t in zip(g,g[1:]+g)]
