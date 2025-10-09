# best: 97(jailctf merger) / others: 99(jacekw Potatoman nauti natte), 101(4atj sisyphus luke Seek mukundan), 102(ox jam), 104(natte), 105(2F)
# ============================================== 97 =============================================

p=lambda g,E=enumerate:[[all([0,*s,0][j:j+3]+[0,*t,0][i:i+3])*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
