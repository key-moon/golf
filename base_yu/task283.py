# best: 82(jailctf merger) / others: 88(intgrah jimboko awu macaque sammyuri), 94(Code Golf International), 94(4atj sisyphus luke Seek mukundan), 94(ox jam), 94(biz)
# ====================================== 82 ======================================
# p=lambda g:[[t[i]and(4<<sum([*t[i-1:i]+t[i+1:i+2]]+s[j-1:j]+s[j+1:j+2]))%7 for j,t in enumerate(zip(*g))]for i,s in enumerate(g)]
# p=lambda g,E=enumerate:[[t[i]and sum([*t[i-1:i+2]]+s[j-1:j+2])**4%7 for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[t[i]and sum([0,*t][i:i+3]+[0,*s][j:j+3])**4%7 for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[t[i]*sum([0,*t][i:i+3]+[0,*s][j:j+3])**4*3%7for j,t in E(zip(*g))]for i,s in E(g)]

# { 20:1, 25:4, 30:2 }
# 5 * { 20:3, 25:5, 30:6 }
