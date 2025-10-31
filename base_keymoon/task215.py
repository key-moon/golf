# best: 42(Code Golf International, FuunAgent, jailctf merger) / others: 44(lv1.dev), 44(biz), 44(intgrah jimboko awu macaque sammyuri), 45(LogicLynx), 45(ox jam)
# p=lambda g,a=2:[max(g[(a:=(a+1)%3)::3])for _ in g] 50
# p=lambda g:[max(g[i%3::3])for i in range(len(g))] 49
# p=lambda g:[max((g:=[[],[]]+g)[2::3])for r in g]
# p=lambda g:[max((g:=[[]]*2+g)[2::3])for r in g]
# p=lambda g:[max((g:=[r,[]]+g)[2::3])for r in g]
# ================== 42 ==================
p=lambda g:[max((g:=g[:2]+g)[2::3])for r in g]
