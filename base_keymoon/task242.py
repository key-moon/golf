# best: 54(cubbus, jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, ALE-Agent, santa2024, FuunAgent, natte, kabutack, JRKXK, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, THUNDER THUNDER, biz, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 55(adakoda), 56(jacekwl Potatoman nauti), 56(jacekw Potatoman nauti), 56(kambarakun), 56(Yuchen20)
# def p(g):B=next(i for(i,r)in enumerate(g)if 0 in r);C=g[B].index(0);D=len(g);return[[g[B+i][D-C-j-1]for j in A(3)]for i in A(3)]
# p=lambda g:list(map(list,zip(*[iter([int(b) for a,b in zip(str(g).replace(" ",""),str(g).replace(" ","")[::-1]) if a=="0"])]*3)))

# p=lambda g:[[b for a,b in zip(r,r[::-1]) if a==0] for r in g if 0in r]
# p=lambda g:[s[r.index(0):][:3]for r in g if 0in(s:=r[::-1])]
# p=lambda g:[r[::-1][r.index(0):][:3]for r in g if 0in r]
# p=lambda g:[r[-r.index(0)-1::-1][:3]for r in g if 0in r]
# p=lambda g:[r[15-r.index(0)::-1][:3]for r in g if 0in r]
# ====================================================
p=lambda g:[r[15-r.index(0)::-1][:3]for r in g if 0in r]
