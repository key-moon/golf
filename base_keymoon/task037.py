# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 109(ox jam), 111(import itertools), 117(intgrah jimboko awu macaque sammyuri), 123(adakoda), 124(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================================= 105 =================================================
# port re;p=lambda g,c=-63:g*c or eval(re.sub("(?<=([^0]).{34})0(?=(.{35})*.{34}\\1)",r"\1",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-9:g*c or eval(re.sub(r"(?<=([^0]).{34})(?=0(.{35})*(?<=\1))",r"\1+",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-25:g*c or eval(re.sub(r"(([^0]).{34})0(?=(.{35})+(?<=\2))",r"\1\2",str(p(g,c+1))))[::-1]
# port re;p=lambda g,c=-45:g*c or eval(re.sub(r"(([^0]).{34})0((.{35})+(?<=\2))",r"\1\2\3",str(p(g,c+1))))[::-1]
import re;p=lambda g,c=-25:g*c or eval(re.sub(r"(([^0]).{34})0(?=(.{35})+(?<=\2))",r"\1\2",str(p(g,c+1))))[::-1]
