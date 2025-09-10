# best: 105(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 130(xsot ovs att joking mewheni), 167(intgrah jimboko awu macaque sammyuri), 170(natte), 194(Potatoman), 194(jacekwl Potatoman nauti)
# ================================================= 105 =================================================
p=lambda g,c=-1,E=enumerate:c*g or p([[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)],c+1)

# def p(g,E=enumerate):
#  for _ in 0,1:
# #   g=[[s[j] or ((2in s)+(3in t)+(0<sum(s[:j])<sum(s))+(0<sum(t[:i])<sum(t))+6)&8 for j,t in E(zip(*g))]for i,s in E(g)]
#   g=[[s[j]or(2in s)+(3in t)+(0<sum(s[:j]+[*t[:i]])<sum(s+[*t]))+6&8for j,t in E(zip(*g))]for i,s in E(g)]
#  return g
