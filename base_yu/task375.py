# best: 53(ovs, luke, mukundan, 4atj, kabutack, sisyphus) / others: 59(Seek64), 62(nauti), 64(el_presidente), 64(rucin93), 64(scpchicken)
# ======================== 53 =======================
# p=lambda g,E=enumerate:[[v*((i-j)*(i+j-len(g)+1)!=0)for j,v in E(s)]for i,s in E(g)]
def p(g):
 for i,s in enumerate(g):s[i]=s[~i]=0
 return g
# p=lambda g:exec("for i,s in enumerate(g):s[i]=s[~i]=0")or g