# best: 101(mukundan) / others: 104(joking+MWI), 104(joking/MWI), 104(joking), 104(joking MeWhenI), 104(natte)
# =============================================== 101 ===============================================
# port re;p=lambda g:(s:="[^0]"+"."*(len(g[0])*3+1)+"[^0]")and eval(re.sub(rf"(?<={s}, )[^0](?=, {s})","8",str(g)))
# mport re;p=lambda g:(s:=(t:="[^0]")+"."*(len(g[0])*3+1)+t)and eval(re.sub(rf"(?<={s}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0]')+'.'*(len(g[0])*3+1)+t)}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0]')+'...'*len(g[0])+'.'+t)}, ){t}(?=, {s})","8",str(g)))
# port re;p=lambda g:eval(re.sub(rf"(?<={(s:=(t:='[^0].')+'...'*len(g[0])+t)} ){t}(?= {s})","8,",str(g)))
import re;p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},){t}(?=,{s})",'8',str(g)))
