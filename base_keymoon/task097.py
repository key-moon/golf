# best: 108(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 113(ox jam), 117(4atj sisyphus luke Seek mukundan), 117(jacekw Potatoman nauti), 136(Yuchen20), 141(dbdr)
# ================================================== 108 ===================================================
# lambda g,E=enumerate:[[v*(1<str([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3]).count(str(v)))for j,v in E(r)]for i,r in E(g)]
p=lambda g,E=enumerate:[[v*(v<sum(sum([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3],())))for j,v in E(r)]for i,r in E(g)]
