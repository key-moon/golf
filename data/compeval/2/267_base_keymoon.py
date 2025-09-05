# best: 48(luke) / others: 50(4atj), 51(mukundan), 53(joking+MWI), 53(joking), 56(kg583)
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:eval((a:=str(g)).replace(a[xx],a[xx]).replace(a[xx],"0"))
# lambda g:[[[*{*g[6][::-1]}][v==max(g[1])]for v in s]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# lambda g:[[0]+[v and g[6][0]for v in s]for _,*s in g]
# lambda g:[[v and g[6][0]for v in[0]+s]for _,*s in g]
# lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
# ===================== 48 =====================
p=lambda g:[[(0<v)*g[6][0]for v in[0]+s]for _,*s in g]
