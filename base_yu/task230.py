# best: 115(jailctf merger) / others: 119(4atj sisyphus luke Seek), 119(sisyphus), 123(mukundan), 126(xsot ovs att joking mewheni), 126(joking MeWhenI)
# ====================================================== 115 ======================================================
# p=lambda g,c=3:-c*g or p([*zip(*[[s[i] or ([t[i-1],t[i],s[i-1]]==[5,0,0] and (3<<c)%5) for i in range(len(s))]for t,s in zip(g[:1]+g,g)][::-1])],c-1)
# p=lambda g,c=3:-c*g or p([*zip(*[[s[i]+(t[i]<t[i-1]-4-s[i-1])*(3<<c)%5for i in range(len(s))]for t,s in zip(g[:1]+g,g)][::-1])],c-1)


import re;p=lambda g,c=3:-c*g or p([*zip(*eval(re.sub(r"(?<=5, 0.{%d}0, )0"%(len(g)*3-2),str((3<<c)%5),str(g)))[::-1])],c-1)
