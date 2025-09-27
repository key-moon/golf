# best: 90(biz) / others: 93(jailctf merger), 95(intgrah jimboko awu macaque sammyuri), 99(4atj sisyphus luke Seek mukundan), 100(ox jam), 101(JRKX)
# ========================================== 90 ==========================================
# p=lambda g,c=-3,E=enumerate:c*g or p([[s[j]or(4in s[j:j+3]and 4in t[i:i+3])*7for j,t in E(g[::-1])]for i,s in E(zip(*g[::-1]))],c+1)
# p=lambda g,c=-3,E=enumerate:c*g or p([[s[j]or(4in s[j:j+3]and 4in t[i:i+3])*7for j,t in E(g)]for i,s in E(zip(*g))][::-1],c+1)
# p=lambda g,c=-3,E=enumerate:c*g or p([[s[j]or any(s[j:j+3])*any(t[i:i+3])*7for j,t in E(g)]for i,s in E(zip(*g))][::-1],c+1)
# p=lambda g,i=-1,E=enumerate:i<0and[[s[j]or p(s,j)*p(t,i)*7for j,t in E(zip(*g))]for i,s in E(g)]or any([0,0,*g][i:i+5])
p=lambda g,E=enumerate:[[s[j]or any([0,0,*s][j:j+5])*any([0,0,*t][i:i+5])*7for j,t in E(zip(*g))]for i,s in E(g)]
