import re
p=lambda g:[[int(re.findall('([1-9]), 0[^[]+\\1',str(g))[0][0])]]