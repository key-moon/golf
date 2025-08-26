# best: 88(mukundan) / others: 90(4atj sisyphus luke Seek), 90(4atj), 94(kabutack), 96(joking+MWI), 96(joking/MWI)
# ========================================= 88 =========================================
import re
p=lambda g,c=-3:c*g or p([*zip(*eval(re.sub("([1-9])((, 0)+, )8","\\1\\2\\1",str(g)))[::-1])],c+1)