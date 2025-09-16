# best: 105(4atj sisyphus luke Seek mukundan) / others: 108(jailctf merger), 109(xsot ovs att joking mewheni), 136(jonas ryno kg583), 144(MasukenSamba), 160(Yuchen20)
# ================================================= 105 =================================================
# port re;p=lambda g,c=-63:g*c or eval(re.sub("(?<=([^0]).{34})0(?=(.{35})*.{34}\\1)",r"\1",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-9:g*c or eval(re.sub(r"(?<=([^0]).{34})(?=0(.{35})*(?<=\1))",r"\1+",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-25:g*c or eval(re.sub(r"(([^0]).{34})0(?=(.{35})+(?<=\2))",r"\1\2",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-45:g*c or eval(re.sub(r"(([^0]).{34})0((.{35})+(?<=\2))",r"\1\2\3",str(p(g,c+1))))[::-1]
import re;p=lambda g,c=-25:g*c or eval(re.sub(r"(([^0]).{34})0(?=(.{35})+(?<=\2))",r"\1\2",str(p(g,c+1))))[::-1]
