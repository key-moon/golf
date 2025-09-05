# best: 51(luke, sisyphus) / others: 52(kg583), 52(mukundan), 52(Seek64), 52(4atj), 52(duckyluuk)
# 残念ながらsum(g,[])するとだめ
# lambda g:[[*(str(g).count("1, 1")//2*"1").ljust(5,"0")]] <- アイデアレベル

# lambda g:[[*(b:=str(g).count("1, 1")//2)*[1],*[0]*(5-b)]]
# lambda g:[(b:=str(g[::2]).count("1, 1"))*[1]+[0]*(5-b)]
# lambda g:[[*str(g[::2]).count("1, 1")*[1],*[0]*5][:5]]
# lambda g:[[*str(g).count("1, 1")//2*[1],0,0,0,0][:5]]
# lambda g:[(b:=str(g).count("1, 1")//2)*[1]+[0]*(5-b)]
# lambda g:[[*str(g).count("1, 1")//2*[1],*[0]*5][:5]] 53
# ======================= 51 ======================
p=lambda g:[[*str(g).count("1, 1")//2*[1],*[0]*5][:5]]
