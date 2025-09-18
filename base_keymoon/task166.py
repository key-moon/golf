# best: 61(4atj sisyphus luke Seek mukundan) / others: 63(jailctf merger), 65(natte), 65(ox jam), 65(intgrah jimboko awu macaque sammyuri), 65(HETHAT)
# 70
# p=lambda g:[[c or(any(s)+any(r))&2for c,s in zip(r,zip(*g))]for r in g]
# 65
# lambda g:[[8%(t+any(s)+any(r)+1)for*s,t in zip(*g,r)]for r in g]
# lambda g:[[(any(s)+any(r)-t&26)%9for*s,t in zip(*g,r)]for r in g]
# lambda g:[[s[0]or(any(s)+any(r))&2for s in zip(r,*g)]for r in g]
# lambda g:[[t or any(s)+any(r)&2for*s,t in zip(*g,r)]for r in g]
# ============================ 61 ===========================
p=lambda g:[[s[0]or any(s)+any(r)&2for s in zip(r,*g)]for r in g]
