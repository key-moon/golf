# best: 83(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 86(xsot ovs att joking mewheni), 99(natte), 107(jonas ryno kg583), 142(Yuchen20), 152(Bulmenisaurus)
# ======================================= 83 ======================================
# import re;p=lambda g,c=4:c and p([*zip(*eval(re.sub("1, 0",f"1,{"8726"[c-1]}",str(g)))[::-1])],c-1)or g
# lambda g,c=4:c and p([[[y,6,8,7,2][(x==1)*c]for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
# lambda g,c=-3:c*g or[*zip(*eval(str(p(g,c+1)).replace("1,","1,%s+"%"6278"[c])))][::-1]
# lambda g,c=3:-c*g or[*zip(*eval(str(p(g,c-1)).replace("1,",f"1,5**{c}*6%11+")))][::-1]
p=lambda g,c=-3:c*g or[*zip(*eval(str(p(g,c+1)).replace("1, 0","1,"+"6278"[c])))][::-1]

# %10みたいなのが絡むのがあったら式をreplaceするやつで縮められる

# mapping = {0: 2, -1: 7, -2: 8, -3: 6}
# mapping = {0: 2, 1: 7, 2: 8, 3: 6}
# mapping = {0: 6, -1: 8, -2: 7, -3: 2}
# mapping = {0: 6, 1: 8, 2: 7, 3: 2}









