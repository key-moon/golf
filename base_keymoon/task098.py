# best: 64(ox jam) / others: 72(jailctf merger), 74(Code Golf International), 88(FuunAgent), 90(4atj sisyphus luke Seek mukundan), 96(LogicLynx)
# 類題: 120 なんだけど 120 のが 3 長い 同じ色の長方形がないことを使う?
# port re;p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},){t}(?=,{s})",'0',str(g)))
# ============================= 64 =============================
# port re;p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},)..(?=,{s})",'0',str(g)))
# .[^0].......[^0]
# port re;p=lambda g:eval(re.sub("(?<="+(s:='[^0]..{%d}[^0]'%len(g[0]*3))+", ).(?=, %s)"%s,'0',str(g)))
# port re;p=lambda g:eval(re.sub("(?<=%s, ).(?=, %s)"%(s:='[^0]..{%d}[^0]'%len(g[0]*3),s),'0',str(g)))
# port re;p=lambda g:eval(re.sub(f"(?<={(s:='[^0]..{%d}[^0]'%len(g[0]*3))}, ).(?=, {s})",'0',str(g)))
import re;p=lambda g:eval(re.sub(rf"(?<=(\d).{(C:='.'*-~len(g[0])*3)})\1(?=.{C}\1)",'0',str(g)))
