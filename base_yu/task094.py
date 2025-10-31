# best: 96(jailctf merger) / others: 97(ox jam), 102(Code Golf International), 102(4atj sisyphus luke Seek mukundan), 102(HIMAGINE THE FUTURE.), 105(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ============================================= 96 =============================================
# p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]==1or(s[j-2:j+3:4]+[t[i-2]]==[1]*3or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)],c+1)
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]&1or(s[j-2:j+3:4]+[t[i-2]]==[1]*3or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)])
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]&1or(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])*6or s[j]for j,t in E(zip(*g))]for i,s in E(g)])
# p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]-~-s[j]%5*(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])for j,t in E(zip(*g))]for i,s in E(g)])
p=lambda g,E=enumerate:g*(6in g[0])or p([[s[j]+6%-s[j]*(s[j-2:j+3:4]==[t[i-2]<2]*2or 6in s+[*t])for j,t in E(zip(*g))]for i,s in E(g)])
