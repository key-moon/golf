# best: 88(mukundan) / others: 90(4atj sisyphus luke Seek), 90(4atj), 94(kabutack), 96(joking+MWI), 96(joking/MWI)
# ========================================= 88 =========================================
# import re
# p=lambda g,c=-3:c*g or p([*zip(*eval(re.sub("([1-9])((, 0)+, )8","\\1\\2\\1",str(g)))[::-1])],c+1)


# p=lambda g,c=-3:c*g or p([(l:=s[0],1)and[[v,l or v][v==8 and ((l:=0) or 1)]for v in s]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or p([(l:=0)or[[v,(1-l)*s[0] or v][l:=l or v==8]for v in s]for s in zip(*g[::-1])],c+1)

