# best: 63(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 64(2F), 64(biz), 70(xsot ovs att joking mewheni), 81(HETHAT), 81(jonas ryno kg583)
# ============================= 63 ============================
# p=lambda g:[[c:=max(g[2])]*10,[c,*[0]*8,c]]*2
# p=lambda g:[[c:=max(g[(i>4)*5+2]),*[c*(645>>i&1)]*8,c]for i in range(10)]
p=lambda g:[[c:=max(g[i-i%5^2]),*[c*(645>>i&1)]*8,c]for i in range(10)]
# p=lambda g,i=0:[[c:=max(g[i-i%5^2]),*[c*(1290>>(i:=i+1)&1)]*8,c]for _ in g]
# p=lambda g:[[c:=max(s),*[c*(645>>i&1)]*8,c]for i,s in enumerate([g[2]]*5+[g[7]]*5)]
# p=lambda g,v=1290:[[c:=max(s),*[c*((v:=v>>1)&1)]*8,c]for s in [g[2]]*5+[g[7]]*5]


# { 1:7, 0:2 }
# { 0:1,2:1,7:1,9:1, 1:0,3:0,4:0,5:0,6:0,8:0 }












