# best: 54(ox jam, 4atj sisyphus luke Seek mukundan, MasukenSamba, kabutack, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, jacekwl, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583) / others: 56(duckyluuk), 56(HETHAT), 64(natte), 64(Potatoman), 64(J&R)
# p=lambda g:[[v*(i==len(s)//2)for i,v in enumerate(s)]for s in g]
# lambda g:[(a:=[0]*(b:=len(s)//2))+[s[b],*a]for s in g]
# ======================== 54 ========================
p=lambda g:[[0]*(b:=len(s)//2)+[s[b]]+b*[0]for s in g]
