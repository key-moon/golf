# best: 78(ox jam) / others: 85(jailctf merger), 89(Code Golf International), 99(jacekw Potatoman nauti natte), 99(import itertools), 99(HIMAGINE THE FUTURE.)
# port re;p=lambda g:(s:="[^0]"+"."*(len(g[0])*3+1)+"[^0]")and eval(re.sub(rf"(?<={s}, )[^0](?=, {s})","8",str(g)))
# mport re;p=lambda g:(s:=(t:="[^0]")+"."*(len(g[0])*3+1)+t)and eval(re.sub(rf"(?<={s}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0]')+'.'*(len(g[0])*3+1)+t)}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0]')+'...'*len(g[0])+'.'+t)}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0].')+'...'*len(g[0])+t)} ){t}(?= {s})","8,",str(g)))
# port re;p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},){t}(?=,{s})",'8',str(g)))
# ==================================== 78 ====================================

# 1      1
#  1  →  0
#   1      1

# 注意
# 1   | ,
#  0  |  ,
#   1 |   ,

# port re;p=lambda g:eval(re.sub(rf"(?<=([1-9]).{{{(C:=len(g[0])*3+4)}}})\1(?=.{{{C}}}\1)",'8',str(g)))
# port re;p=lambda g:eval(re.sub(r"(?<=([1-9]).{%s})\1(?=.{%s}\1)"%(C:=len(g[0])*3+4,C),'8',str(g)))
import re;p=lambda g:eval(re.sub(rf"(?<=([1-9]){(C:='.'*(len(g[0])*3+4))})\1(?={C}\1)",'8',str(g)))
