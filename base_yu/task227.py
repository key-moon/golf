# best: 52(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 54(intgrah jimboko awu macaque sammyuri), 55(4atj sisyphus luke Seek mukundan), 57(HETHAT), 60(cubbus), 60(Yuchen20)
# ======================= 52 =======================
# p=lambda g:[[2-2*(x|y>0)for x,y in zip(*c)]for c in zip(g,g[4:])]
# p=lambda g:[*eval("[2-2*(x|y>0)for x,y in zip(g.pop(0),g[3])],"*4)]
# p=lambda g:[*eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)]
p=lambda g:eval("[2*(x+y<1)for x,y in zip(g.pop(0),g[3])],"*4)
# p=lambda g:[[2*(g[i][j]==g[i+4][j]<1)for j in range(4)]for i in range(4)]
