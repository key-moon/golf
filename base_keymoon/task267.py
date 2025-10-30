# best: 46(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, adakoda) / others: 52(ox jam), 54(cubbus), 54(Tony Li), 54(Tony Li & Darren Amadeus Martin), 54(HIMAGINE THE FUTURE.)
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:eval((a:=str(g)).replace(a[xx],a[xx]).replace(a[xx],"0"))
# lambda g:[[[*{*g[6][::-1]}][v==max(g[1])]for v in s]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s]for _,*s in g]
# lambda g:[[v and g[6][0]for v in[0]+s]for _,*s in g]
# lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
# ==================== 46 ====================
p=lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
