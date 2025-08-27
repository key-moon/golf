# best: 98(mukundan) / others: 100(luke/sisyphus/Seek), 100(4atj sisyphus luke Seek), 100(natte), 100(sisyphus), 101(xsot ovs)
# 類題: 120 なんだけど 120 のが 3 長い 同じ色の長方形がないことを使う?
# ============================================== 98 ==============================================
import re;p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},){t}(?=,{s})",'0',str(g)))
