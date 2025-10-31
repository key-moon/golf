# best: 92(Code Golf International) / others: 100(ox jam), 105(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 105(4atj sisyphus luke Seek mukundan), 105(jailctf merger), 105(HIMAGINE THE FUTURE.)
# =========================================== 92 ===========================================
# p=lambda g,E=enumerate:[[8*(8in{*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[max({*s[:j]}&{*s[j:]}|{*t[:i+1]}&{*t[i:]})for j,t in E(zip(*g))]for i,s in E(g)]
