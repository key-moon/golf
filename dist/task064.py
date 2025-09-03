import re
def p(g):u=sum(g,g[5]);c,d,e=sorted({*u},key=u.count);return eval('(g:=[*zip(*eval(re.sub(f"(?<={c}, ){e}(?=(, \d)*, {d})",str(c),str(g)))[::-1])]),'*80)[-1]