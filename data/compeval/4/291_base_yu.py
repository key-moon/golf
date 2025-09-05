import re
p=lambda g:[[int(re.search('([^0]), 0[^[]+\\1',str(g))[1])]]