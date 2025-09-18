# 類題:254
# best: 68(jailctf merger) / others: 70(4atj sisyphus luke Seek mukundan), 72(ox jam), 72(xsot ovs att joking mewheni), 77(HETHAT), 81(natte)
# =============================== 68 ===============================
# p=lambda g:[*zip(*[[x and 9-sorted(map(sum,zip(*g))).index(sum(s))for x in s]for s in zip(*g)])]
# p=lambda g:[*zip(*[[x and 9-sorted(zip(*g),key=sum).index(s)for x in s]for s in zip(*g)])]
# p=lambda g:[[x and 9-sorted(zip(*g),key=sum).index(t)for x,t in zip(s,zip(*g))]for s in g]
p=lambda g:[[x and 9-sorted(zip(*g),key=sum).index((*t,))for*t,x in zip(*g,s)]for s in g]
# p=lambda g:(u:=[*zip(*g)])and[[s.pop(0)and 9-sorted(u,key=sum).index(t)for t in u]for s in g]
