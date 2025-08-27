import re
p=lambda g:eval(re.sub(f"(?<={(s:=(t:='.[^0]')+'...'*len(g[0])+t)},){t}(?=,{s})",'8',str(g)))