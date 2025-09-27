# best: 80(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 83(ox jam), 93(2F), 93(biz), 104(intgrah jimboko awu macaque sammyuri), 108(jacekwl Potatoman nauti)
# ===================================== 80 =====================================
# p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-(0<sum(t)<3*c))]+s for s,t in zip(g,g[1:]+g)]
