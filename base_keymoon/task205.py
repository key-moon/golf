# best: 166(4atj sisyphus luke Seek mukundan) / others: 170(xsot ovs att joking mewheni), 188(jailctf merger), 202(natte), 254(MasukenSamba), 265(intgrah jimboko awu macaque sammyuri)
# =============================================================================== 166 ================================================================================
# 最小縦横: 6
# 背景色を含まない行を削りながらてんちさいき→しばらく削ったら種類数でも削る
# 矩形のふちは必ず背景色
# ケース96の誤検知回避: max(u:=sum(g,g[-3]),key=u.count))
p=lambda g,c=7:-c*[[[v,sum(S:={*t,*s})-t[0]][len(S)>1]for*t,v in zip(*g,s)]for s in g]or p([*zip(*[r for r in g if(c<4)*len({*r})<4<r.count(max(u:=sum(g,g[-3]),key=u.count))])],c-1)
