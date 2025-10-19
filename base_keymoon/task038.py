# best: 51(jailctf merger, natte, 2F, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, Code Golf International, ox jam, MasukenSamba, intgrah jimboko awu macaque sammyuri, biz, import itertools) / others: 52(kabutack), 52(jonas ryno kg583), 52(JRKKX), 52(blob2822), 52(THUNDER THUNDER)
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

# p=lambda g:[(str(g).count("1, 1")//2*[1]+[0]*5)[:5]]
p=lambda g:[(str(g).count("1, 1")*[1]+[0]*9)[:9:2]]
