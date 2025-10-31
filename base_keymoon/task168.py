# best: 110(Code Golf International, jailctf merger) / others: 111(lv1.dev), 112(4atj sisyphus luke Seek mukundan), 112(ox jam), 114(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 116(jacekw Potatoman nauti natte)
# =================================================== 110 ====================================================
# port re;p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]
# port re;p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+, ([^0]).{28}(\2, ){2})",r"\2",str(p(g,c+1)))))][::-1]
# port re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+, ([^0]).{28}(\2, ){2})",r"\2",str(p(g,c+1)))))][::-1]
import re;p=lambda g,c=-3:c*g or[*zip(*eval(re.sub(r"0(?=(.{35})+(, ([^0])).{26}\2\2)",r"\3",str(p(g,c+1)))))][::-1]

# port re;# p=lambda g:eval(r'(g:=eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1 \2",str(g)))),')[0]
