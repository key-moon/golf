# best: 68(jailctf merger) / others: 70(4atj sisyphus luke Seek mukundan), 72(ox jam), 72(xsot ovs att joking mewheni), 77(HETHAT), 81(natte)
# lambda g:[*zip(*[[(9-sorted(zip(*g)).index(r))*(0<c)for c in r]for r in zip(*g)])]
# =============================== 68 ===============================
# lambda g:[*zip(*[[(9-sorted(zip(*g)).index(r))*c/5for c in r]for r in zip(*g)])]
# lambda g:[[(9-sorted(zip(*g)).index(t[1:]))*t[0]/5for t in zip(r,*g)]for r in g]
# lambda g:[[(9-sorted(zip(*g)).index(t))*c/5for c,t in zip(r,zip(*g))]for r in g]
# lambda g:[[(9-sorted(zip(*g)).index((*t,)))*c/5for*t,c in zip(*g,r)]for r in g]
# lambda g:[[(9-sorted(zip(*g,r)).index(t))*t[9]/5for t in zip(*g,r)]for r in g]
# lambda g,R=[0]*9:[R:=[c/5*(C or max(R)+1)for c,C in zip(r,R)]for r in g]
# lambda g,R=[0]*9:[R:=[r.pop(0)/5*(C or max(R)+1)for C in R]for r in g]
p=lambda g,R=[0]*9:[R:=[r.pop(0)and(C or-~max(R))for C in R]for r in g]
