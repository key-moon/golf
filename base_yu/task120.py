# best: 78(ox jam) / others: 85(jailctf merger), 89(Code Golf International), 99(jacekw Potatoman nauti natte), 99(import itertools), 99(HIMAGINE THE FUTURE.)
# ==================================== 78 ====================================

p=lambda g,E=enumerate:[[all([0,*s,0][j:j+3]+[0,*t,0][i:i+3])*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
