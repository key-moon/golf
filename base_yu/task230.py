# best: 114(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 128(natte), 140(intgrah jimboko awu macaque sammyuri), 141(jacekwl Potatoman nauti), 141(jacekw Potatoman nauti), 142(MasukenSamba)
# ===================================================== 114 ======================================================
# p=lambda g,c=3:-c*g or p([*zip(*[[s[i] or ([t[i-1],t[i],s[i-1]]==[5,0,0] and (3<<c)%5) for i in range(len(s))]for t,s in zip(g[:1]+g,g)][::-1])],c-1)
# p=lambda g,c=3:-c*g or p([*zip(*[[s[i]+(t[i]<t[i-1]-4-s[i-1])*(3<<c)%5for i in range(len(s))]for t,s in zip(g[:1]+g,g)][::-1])],c-1)


# port re;p=lambda g,c=3:-c*g or p([*zip(*eval(re.sub(r"(?<=5, 0.{%d}0, )0"%(len(g)*3-2),str((3<<c)%5),str(g)))[::-1])],c-1)
# mapping = { 0: 1, 1: 2, 2: 4, 3: 3 }
# port re;p=lambda g,c=3:-c*g or p([*zip(*eval(re.sub(r"0(?=, 0.{%d}5, 5)"%-~len(g*3),str(f(c)),str(g[::-1]))))],c-1)
# mapping = { 0: 1, 1: 2, 2: 4, 3: 3 } # 2**a%5
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub(r"0(?=, 0,.{%d}5, 5)"%len(g*3),str(2**c%5),str(p(g,c-1)))))][::-1]
# mapping = { 0: 3, 1: 4, 2: 2, 3: 1 } # (a*9|8)%5
# mapping = { 0: 3, -1: 4, -2: 2, -3: 1 }
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub(r"0(?=, 0,.{%d}5, 5)"%len(g*3),str((c*9|8)%5),str(p(g,c-1)[::-1]))))]
# mapping = { 0: 1, 1: 3, 2: 4, 3: 2 } # 3**x%5&7
# mapping = { 0: 1, -1: 3, -2: 4, -3: 2 }
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub(f"0(?={('.'*(len(g)*3+4)+'5')*2})",str(3**c%5),str(p(g,c-1))))[::-1])]
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub("0(?=(.....{%s}5){2})"%len(g*3),str(3**c%5),str(p(g,c-1))))[::-1])]
# port re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub("0(?=(.{%s}5){2})"%(len(g*3)+4),str(3**c%5),str(p(g,c-1))))[::-1])]
import re;p=lambda g,c=3:-c*g or[*zip(*eval(re.sub("0(?=, 0,.{%s}5, 5)"%len(g*3),"3**c%5",str(p(g,c-1))))[::-1])]
