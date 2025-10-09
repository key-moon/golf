# best: 46(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 50(intgrah jimboko awu macaque sammyuri), 52(ox jam), 54(cubbus), 54(Tony Li), 56(jonas ryno kg583 kabutack)
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:eval((a:=str(g)).replace(a[xx],a[xx]).replace(a[xx],"0"))
# lambda g:[[[*{*g[6][::-1]}][v==max(g[1])]for v in s]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s]for _,*s in g]
# lambda g:[[v and g[6][0]for v in[0]+s]for _,*s in g]
# lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
# ==================== 46 ====================
p=lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
