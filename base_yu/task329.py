# best: 54(mukundan, 4atj sisyphus luke Seek mukundan, jacekwl Potatoman, xsot ovs att joking mewheni, Yuchen20, 4atj sisyphus luke Seek, kabutack, jailctf merger, nauti, MasukenSamba, intgrah jimboko awu macaque sammyuri, jacekwl) / others: 56(duckyluuk), 56(HETHAT), 64(kg583), 64(Potatoman), 64(jonas ryno kg583)
# p=lambda g:[[v*(i==len(s)//2)for i,v in enumerate(s)]for s in g]
# lambda g:[(a:=[0]*(b:=len(s)//2))+[s[b],*a]for s in g]
# ======================== 54 ========================
p=lambda g:[[0]*(b:=len(s)//2)+[s[b]]+b*[0]for s in g]
