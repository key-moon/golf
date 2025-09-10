# best: 57(4atj sisyphus luke Seek mukundan, 2F, biz, jailctf merger, xsot ovs att joking mewheni) / others: 61(intgrah jimboko awu macaque sammyuri), 63(MasukenSamba), 63(kabutack), 63(Yuchen20), 63(jacekwl)

# {*sum(g,[])}
# {*g[0]+g[1]}
# ========================== 57 =========================
# lambda g:[[[*{*sum(g,[])}-{5}][0]*(v==5)for v in r]for r in g]
# lambda g:[[(v==5)*(sum({*sum(g,[])})-v)for v in s]for s in g]
# lambda g:[[[*{0,*sum(g,[])}-{v,v-5}][0]for v in s]for s in g]
# lambda g:[[(sum({*sum(g,[])})-5)*(v==5)for v in r]for r in g]
# lambda g:[[sum({*sum(g,[])}-{5})*(v==5)for v in r]for r in g]
# lambda g:[[sum({*sum(g*(v==5),[])}-{5})for v in r]for r in g]
# lambda g:[[[*{*sum(g,[])}-{v},0][v!=5]for v in r]for r in g]
p=lambda g:[[sum({*sum(g,[-5])})*(v==5)for v in r]for r in g]
