# best: 55(luke) / others: 57(xsot), 61(Seek64), 63(ovs), 63(mukundan), 63(cg)
# ========================= 55 ========================
# p=lambda g:[[[*filter(bool,s[i::5]),0][0]for i in range(4)]for s in g]
# p=lambda g:[[[*filter(bool,c),0][0]for c in zip(s,s[5:],s[10:])]for s in g]
# p=lambda g:[[x or y or z for x,y,z in zip(s,s[5:],s[10:])]for s in g]
# p=lambda g:[[s[i]or s[i+5]or s[i+10]for i in range(4)]for s in g]
# p=lambda g:[[s.pop(0)or s[4]or s[9]for _ in[0]*4]for s in g]
p=lambda g:[[*eval("s.pop(0)or s[4]or s[9],"*4)]for s in g]