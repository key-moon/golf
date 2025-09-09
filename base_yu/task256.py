# best: 95(jailctf merger) / others: 96(xsot ovs att joking mewheni), 98(4atj sisyphus luke Seek mukundan), 98(4atj sisyphus luke Seek), 106(intgrah jimboko awu macaque sammyuri), 107(natte)
# ============================================= 95 ============================================
# p=lambda g,E=enumerate:[[([2-(i<k)+(i>k)]*(i+s.count(2)-k)+[0]*99)[:len(t)]for k,t in E(g)]for i,s in E(g)if 2in s][0]
# p=lambda g,E=enumerate:[[([2-(i<k)+(i>k)]*(i+sum(s)//2-k)+[0]*99)[:len(t)]for k,t in E(g)]for i,s in E(g)if 2in s][0]
# p=lambda g,E=enumerate:(i:=[*zip(*g)][0].index(2))and[[(2-(i<k)+(i>k))*(k+l<i+sum(g[i])//2)for l,_ in E(t)]for k,t in E(g)]
p=lambda g,E=enumerate:[[(2-((i:=g.index(max(g)))<k)+(i>k))*(k+l<i+sum(g[i])//2)for l,_ in E(t)]for k,t in E(g)]
# p=lambda g,E=enumerate:[[[(2-(i<k)+(i>k))*(k+l<i+sum(s)//2)for l,_ in E(t)]for k,t in E(g)]for i,s in E(g)if 2in s][0]
# p=lambda g,E=enumerate:[[(2-((i:=[*zip(*g)][0].index(2))<k)+(i>k))*(k+l<i+sum(g[i])//2)for l,_ in E(t)]for k,t in E(g)]
