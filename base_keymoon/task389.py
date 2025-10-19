# best: 57(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, biz, import itertools) / others: 58(Yuchen20), 61(intgrah jimboko awu macaque sammyuri), 62(kambarakun), 62(cg-klogw), 62(cg-klogw-sekken)

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
