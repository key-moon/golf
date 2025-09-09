# best: 50(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 54(duckyluuk), 54(intgrah jimboko awu macaque sammyuri), 54(HETHAT), 56(kabutack), 56(jonas ryno kg583)
# p=lambda g:[[6*any(s)for s in zip(*zip(*[iter(r)]*3))]for r in g]
# p=lambda g:[[6*(0<sum(s))for s in zip(r,r[3:])]for r in g]
# p=lambda g:[[6*(0<a+b)for a,b in zip(r,r[3:])]for r in g]
# p=lambda g:[[6*(0<r[i]+r[i+3])for i in(0,1,2)]for r in g]
# p=lambda g:[[6*any(r[i::3])for i in(0,1,2)]for r in g]
# p=lambda g:[[6*any(s)for s in zip(r,r[3:])]for r in g]
# in range(3)
# in(0,1,2)
# in b"012"
# 3,4 -> 6
# lambda g:[[               for s in r]for r in g]
# lambda g:[[          for i in(0,1,2)]for r in g]
# lambda g:[[    for s in zip(r,r[3:])]for r in g]
# ====================== 50 ======================
p=lambda g:[[6*any(r[i::3])for i in(0,1,2)]for r in g]


