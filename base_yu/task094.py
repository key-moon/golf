# best: 98(jailctf merger) / others: 102(4atj sisyphus luke Seek mukundan), 106(ox jam), 116(jacekw Potatoman nauti natte), 116(jacekw Potatoman nauti), 117(intgrah jimboko awu macaque sammyuri)
# ============================================== 98 ==============================================
# p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]==1or(s[j-2:j+3:4]+[t[i-2]]==[1]*3or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)],c+1)
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]&1or(s[j-2:j+3:4]+[t[i-2]]==[1]*3or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)])
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]&1or(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)])
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]-~-s[j]%5*(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])for j,t in E(zip(*g))]for i,s in E(g)])
p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]+6%-s[j]*(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])for j,t in E(zip(*g))]for i,s in E(g)])
