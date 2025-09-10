# best: 186(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 208(xsot ovs att joking mewheni), 211(jonas ryno kg583), 222(MasukenSamba), 235(intgrah jimboko awu macaque sammyuri), 243(JRK)
# ========================================================================================= 186 ==========================================================================================
# ブロック: 2-6
# 243
# def p(g):
#  w=len(g[0])
#  _,n,s={*(t:=bytes(sum(g,[])))}
#  if 5<str(g).count(f" {n},"*2):n,s=s,n
# #  W=(len(t)-t[::-1].index(s)-(I:=t.index(s)))//w//3+1
#  W=(t.rfind(s)-(I:=t.find(s)))//w//3+1
#  return [[[0,n][g[i][j]==s]for j in range(min((*a,s).index(s)for a in g),99,W)[:3]] for i in range(I//w,99,W)[:3]]
# 233
def p(g):
 n,s={*sum(g,[])}-{0}
 if 5<str(g).count(f" {n},"*2):n,s=s,n
 e=lambda g:range(l:=min((*a,s).index(s)for a in g),h:=max(bytes(a).rfind(s)for a in g),(h-l+1)//3)
 return [[[0,n][g[i][j]==s]for j in e(g)] for i in e([*zip(*g)])]








