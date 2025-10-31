# best: 51(ox jam) / others: 52(Code Golf International), 52(jailctf merger), 56(jacekw Potatoman nauti natte), 56(4atj sisyphus luke Seek mukundan), 56(lv1.dev)
# ======================= 51 ======================
# p=lambda g:[[v+2*(v>0)*(i%3<1)for i,v in enumerate(s)]for s in g]
p=lambda g:[[v*i/2for v,i in zip(s,b""*9)]for s in g]
