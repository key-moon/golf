# best: 87(jailctf merger) / others: 91(4atj sisyphus luke Seek mukundan), 93(xsot ovs att joking mewheni), 106(natte), 107(kabutack), 147(MasukenSamba)
# ========================================= 87 ========================================
p=lambda g,c=-3:c*g or p([[y or(-x%21-x|x)%9for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)

# 0 -> 0
# 1,2 -> 1
# 4,8 -> 4
# 6,3 -> 6


# mapping = { 0:0, 1:1, 2:1, 4:4, 8:4, 3:6, 6:6 }







