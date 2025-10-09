# Input:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 5 0 5 0
# 5 5 5 5 5
# Output:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 5 0 5 0
# 5 1 5 1 5
# def p(g):
#  for val_r in g[:-1]:
#   for val_x,val_v in enumerate(val_r):
#    if val_v==1:val_r[val_x]=0;g[-1][val_x]=1
#  return g
# 改善の余地ありそう 1を消し飛ばすところが雑
# p=lambda g:eval(str(g[:-1]).replace("1","0"))+[[next(filter(None,z))for z in zip(*g)]]
# p=lambda g:eval(f"{g[:-1]}".replace("1","0"))+[[next(filter(None,z))for z in zip(*g)]]
# 1以上で最小の値を持ってくる
# next(filter(None,z))
# min([a for a in z if a])
# p=lambda g:[*eval(f"{g[:-1]}".replace("1","0")),[min(filter(int,z))for z in zip(*g)]]
# best: 46(jacekwl Potatoman nauti, jacekw Potatoman nauti natte, blob2822, 4atj sisyphus luke Seek mukundan, Afordancja, HETHAT, jacekw Potatoman nauti, natte, MasukenSamba, jailctf merger, Yuchen20, ox jam, duckyluuk, intgrah jimboko awu macaque sammyuri) / others: 47(jonas ryno kg583 kabutack), 47(JRKX), 47(JRKXK), 47(Tony Li), 47(JRKKX)
# ============================================
# p=lambda g:[*[g[0]]*3,g[3],[min(filter(int,z))for z in zip(*g)]]
# p=lambda g:[*[g[0]]*3,g[3],[[5,1][c]for c in g[2]]]
p=lambda g:g[:1]*3+[g[3],[5-c*4for c in g[2]]]
