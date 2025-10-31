# best: 134(jailctf merger) / others: 136(ox jam), 144(Code Golf International), 153(HIMAGINE THE FUTURE.), 161(intgrah jimboko awu macaque sammyuri), 166(4atj sisyphus luke Seek mukundan)
# =============================================================== 134 ================================================================
# 最小縦横: 6
# 背景色を含まない行を削りながらてんちさいき→しばらく削ったら種類数でも削る
# 矩形のふちは必ず背景色
# ケース96の誤検知回避: max(u:=sum(g,g[-3]),key=u.count))
# p=lambda g,c=7:-c*[[[v,sum(S:={*t,*s})-t[0]][len(S)>1]for*t,v in zip(*g,s)]for s in g]or p([*zip(*[r for r in g if(c<4)*len({*r})<4<r.count(max(u:=sum(g,g[-3]),key=u.count))])],c-1)
# p=lambda g,c=-99:c*[[[s[0],sum(S:={*s,*t})-s[0]][S>{s[0]}]for t in zip(*g)]for s in g] or p([*zip(*g[any(bytes([c]*5)in bytes(g[-1])for c in g[-1])-2::-1])],c+1)
p=lambda g,c=-99:c*[[[v,sum(S:={*s,*t})-v][S>{v}]for*t,v in zip(*g)]for s in g]or p([*zip(*g[any(bytes([c]*5)in bytes(g[-1])for c in g[-1])-2::-1])],c+1)
