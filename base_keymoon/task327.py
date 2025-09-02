# best: 67(xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 69(mukundan), 74(kabutack), 88(Bulmenisaurus), 89(natte), 106(MasukenSamba)
# =============================== 67 ==============================
# lambda g,a=[0]*3,S=[0]*6:[S:=[*map(max,zip(s+a,[0]+S))]for s in g+[a]*3]
# f p(g):S=(b:=[0])*6;return[S:=[*map(max,zip(s+b*3,b+S))]for s in g+[b*3]*3]
# lambda g,S=(b:=[0])*6:[S:=[*map(max,zip(s+b*3,b+S))]for s in g+[b*3]*3]
p=lambda g,S=(a:=[0]*3)*2:[S:=[*map(max,zip(s+a,[0]+S))]for s in g+[a]*3]
