# best: 51(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, MasukenSamba, jailctf merger, HIMAGINE THE FUTURE., ox jam, 2F, biz, intgrah jimboko awu macaque sammyuri) / others: 52(jonas ryno kg583 kabutack), 52(cubbus), 52(jacekwl Potatoman nauti), 52(JRK), 52(blob2822)
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
