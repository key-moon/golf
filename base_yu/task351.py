# best: 67(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 68(jacekwl Potatoman nauti), 68(xsot ovs att joking mewheni), 80(kabutack), 81(jonas ryno kg583), 82(cg)
# =============================== 67 ==============================
# 400と同じ問題
# p=lambda g,R=range(16):[*filter(len,[[g[15-i][15-j]for j in R if g[i][j]==3]for i in R])]
# p=lambda g,R=range(16):[u for i in R if(u:=[g[~i][~j]for j in R if g[i][j]==3])]
p=lambda g:[(t:=sum(g,[]))[~t.index(3)-i*16::-1][:5]for i in range(5)]


# p=lambda g,R=range(16):[[g[~i][~j]for j in R if g[i][j]==3]for i in R if 3 in g[i]]
# p=lambda g:[u for s,t in zip(g,g[::-1]) if(u:=[y for x,y in zip(s,t[::-1]) if x==3])]
# p=lambda g:[[y for x,y in zip(s,t[::-1]) if x==3]for s,t in zip(g,g[::-1])if 3 in s]

# p=lambda g,R=range(16):[u for x,y in zip(g,g[::-1]) if(u:=[w for v,w in zip(x,y[::-1]) if v==3])]




