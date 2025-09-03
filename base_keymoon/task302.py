# best: 89(4atj sisyphus luke Seek) / others: 92(jailctf merger), 93(xsot ovs att joking mewheni), 97(mukundan), 112(biz), 142(Afordancja)
# import re;lambda g,i=-9:g*i or eval(re.sub(rf"(?<=[^0].{{{len(g[0])*3-2}}}5, )"+"0, "*(a:=4+i//3),f"9{a-4},"*a,str(p(g,i+1))))
# min(g)
# ========================================== 89 =========================================
# eval("...,"*12)
# [...for _ in r]

# Dは毎回初期化しないと駄目だった
# D>5andなのは短絡評価でr.indexのエラーを回避
# lambda g:[(D:=0)or eval("int(D:=[D>5and[5+r.index(5),D][6<D],5+(D<1)/2][0<r.pop(0)]),"*12)for r in g]
# lambda g:[(D:=0)or[int(D:=[D>5and[5+r.index(5),D][6<D],5+(D<1)/2][0<r.pop(0)])for _ in g]for r in g]
# lambda g:[(D:=0)or[int(D:=r.pop(0)and(D<1)/2+5or D%1and 6+r.index(5)or D%-5%10)for _ in g]for r in g]
# lambda g:[(D:=0)or[int(D:=r.pop(0)and(D<1)/2+5or D%1and 6+r.index(5)or(D>5)*D)for _ in g]for r in g]
p=lambda g:[(D:=0)or[int(D:=r.pop(0)and(D<1)/2+5or D>5and[6+r.index(5),D][6<D])for _ in g]for r in g]

# !=5 →0 なら前のをコピー
#   5→0  なら生成するかしないか決めないとだめ これは追加情報を持たないと判定不能
# int(D:=) とすることにし、Dの小数点以下をマーカーにする
# 5.xからなら許可（index）、5からなら不許可（0）

# 0→5 なら 5.x
# ?→5 なら 5

#  D   c
#  6<  0  D
#  5<  0  index
#  0   0  0
#  6>  5  5
#  0   5  5.x

#  5.1 をマーカーにする 5.1からなら

# 塗る色か、自身か
