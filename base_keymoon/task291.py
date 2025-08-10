# best: 63
import re
p=lambda g:[[int(re.findall(r'([1-9]), 0[^[]+\1',str(g))[0][0])]]

# A=enumerate
# def p(g):
#   match = re.findall(r'([1-9])[^[]+(\1)',str(g))[0]
#   print(match)
#   print(match)
#   return match.group(1) if match else None