# best: 55(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 57(xsot ovs att joking mewheni), 61(HETHAT), 62(intgrah jimboko awu macaque sammyuri), 63(2F), 63(cg)
# ========================= 55 ========================
# lambda g:[[[*filter(bool,c),0][0]for c in zip(s,s[5:],s[10:])]for s in g]
# lambda g:[[next(filter(bool,s[i::5]+[0]))for i in(0,1,2,3)]for s in g]
# lambda g:[[[*filter(bool,s[i::5]),0][0]for i in range(4)]for s in g]
# lambda g:[[x or y or z for x,y,z in zip(s,s[5:],s[10:])]for s in g]
# lambda g:[[s[i]or s[i+5]or s[i+10]for i in range(4)]for s in g]
# lambda g:[[s.pop(0)or s[4]or s[9]for _ in[0]*4]for s in g]
# lambda g:[eval("s.pop(0)or min(s[4::5]),"*4)for s in g]
p=lambda g:[eval("s.pop(0)or s[4]or s[9],"*4)for s in g]
# 55はtuple許可以前に出てたのでもっと縮むはず








