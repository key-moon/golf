# best: 60(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 66(ox jam), 66(HETHAT), 66(xsot ovs att joking mewheni), 67(jonas ryno kg583 kabutack), 67(Yuchen20)
# =========================== 60 ===========================
# lambda g:[(u:=[0]+[2]*sum(sum(g,[]))+[0]*7)[1:4],u[::4],[0]*3]
# lambda g:[(u:=[2]*sum(sum(g,[]))+(b:=[0]*3))[:3],[0,u[3],0],b]
# lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0]+u[3:5],[0]*3]
p=lambda g:[(u:=[2]*sum(sum(g,a:=[0]))+a*9)[:3],a+u[3:5],a*3]
