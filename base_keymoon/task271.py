# best: 86(xsot ovs att joking mewheni) / others: 92(jailctf merger), 96(4atj sisyphus luke Seek mukundan), 105(kabutack), 113(intgrah jimboko awu macaque sammyuri), 115(cg)
# 9x9グリッド 背景: 0
# 要素が{1,8}の 3x3のグリッドが4つ
# 8が一番少ない or 1 が一番多いグリッドを抽出
# p=lambda g:eval(max((a.count("1"),a) for x in range(49) if "0" not in (a:=str([r[x%7:][:3]for r in g[x//7:][:3]])))[1])
# p=lambda g:eval(max((a.count("1"),a) for x in range(49) if "0"not in(a:=str([r[x%7:][:3]for r in g[x//7:][:3]])))[1])
# アイデア: zip(g,g[1:],g[2:]) みたいなことすると伸びるかも
# p=lambda g:max((str(a).count('1'),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# p=lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# p=lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# ============================================================================================

# lambda g:min((sum(sum(a,[])),a)for x in range(49)if 0<min(min(a:=[r[x%7:][:3]for r in g[x//7:][:3]])))[1]
# lambda g:len(g)==3and(sum(a:=sum(g,()))+0**min(a)*99,g)or min([p([*zip(*g[i:i+3])])for i in range(7)])[1]
# lambda g:min((sum(b),a)for x in range(49)if 0<min(b:=sum(a:=[r[x%7:][:3]for r in g[x//7:][:3]],[])))[1]
# lambda g:min((sum(b:=sum(a:=[r[x%7:][:3]for r in g[x//7:][:3]],[]))+(0in b)*99,a)for x in range(49))[1]
p=lambda g:g*(len(g)<4)or min((sum(a:=sum(b:=p([*zip(*g[i:i+3])]),()))+(0in a)*99,b)for i in range(7))[1]

# ↓keyをlambdaでごまかし系列 カス
# lambda g:(sum(b:=sum(g,[]))+(0in b)*99)*(len(g)<4)or min(([r[x%7:][:3]for r in g[x//7:][:3]]for x in range(49)),key=p)[1]
# lambda g:min(([r[x%7:][:3]for r in g[x//7:][:3]]for x in range(49)),key=lambda g:sum(b:=sum(g,[]))+(0in b)*99)[1]









