# best: 111(jailctf merger) / others: 112(4atj sisyphus luke Seek mukundan), 117(natte), 117(xsot ovs att joking mewheni), 177(MasukenSamba), 189(jonas ryno kg583)
# ==================================================== 111 ====================================================
# port re;p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]
# port re;p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+, ([^0]).{28}(\2, ){2})",r"\2",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+, ([^0]).{28}(\2, ){2})",r"\2",str(p(g,c+1)))))][::-1]
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+(, ([^0])).{26}\2\2)",r"\3",str(p(g,c+1)))))][::-1]

# port re;# p=lambda g:eval(r'(g:=eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1 \2",str(g)))),')[0]

