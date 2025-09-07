# best: 51(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni, mukundan) / others: 52(natte), 52(Potatoman), 52(duckyluuk), 52(jacekwl Potatoman), 52(dbdr)
# 残念ながらsum(g,[])するとだめ
# lambda g:[[*(str(g).count("1, 1")//2*"1").ljust(5,"0")]] <- アイデアレベル

# lambda g:[[*(b:=str(g).count("1, 1")//2)*[1],*[0]*(5-b)]]
# lambda g:[(b:=str(g[::2]).count("1, 1"))*[1]+[0]*(5-b)]
# lambda g:[[*str(g[::2]).count("1, 1")*[1],*[0]*5][:5]]
# lambda g:[[*str(g).count("1, 1")//2*[1],0,0,0,0][:5]]
# lambda g:[(b:=str(g).count("1, 1")//2)*[1]+[0]*(5-b)]
# lambda g:[[*str(g).count("1, 1")//2*[1],*[0]*5][:5]] 53
# ======================= 51 ======================

# p=lambda g:[[*str(g).count("1, 1")//2*[1],*[0]*5][:5]]
# p=lambda g:[(str(g[::2]).count("1, 1")*[1]+[0]*5)[:5]]

p=lambda g:[(str(g).count("1, 1")//2*[1]+[0]*5)[:5]]
