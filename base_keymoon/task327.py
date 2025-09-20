# best: 67(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 74(JRKX), 74(kabutack), 74(HETHAT), 86(Yuchen20), 88(Bulmenisaurus)
# lambda g,a=[0]*3,S=[0]*6:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
# f p(g):S=(b:=[0])*6;return[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# lambda g,S=[0]*6:[S:=[*map(max,s+[0]*9,[0]+S)][:6]for s in g+[S]*3]
# lambda g,S=(b:=[0])*6:[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# =============================== 67 ==============================
p=lambda g,S=(a:=[0]*3)*2:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
