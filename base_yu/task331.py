# best: 83(sisyphus) / others: 88(joking+MWI), 96(mukundan), 99(natte), 100(joking), 101(Seek64)
# ======================================= 83 ======================================
# import re;p=lambda g,c=4:c and p([*zip(*eval(re.sub("1, 0",f"1,{[8,7,2,6][c-1]}",str(g)))[::-1])],c-1)or g
p=lambda g,c=4:c and p([[[y,6,8,7,2][(x==1)*c]for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
