# best: 102(4atj sisyphus luke Seek mukundan) / others: 106(ox jam), 113(jailctf merger), 116(jacekw Potatoman nauti natte), 116(jacekw Potatoman nauti), 117(intgrah jimboko awu macaque sammyuri)
# =============================================== 102 ================================================
# port re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub(r"8(?=[^(]+\(.{,40}1.{43}1, 1)","6",str(p(g,c+1)))))]
import re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub(r"8(?=[^(]*\([^(]*1.{43}1, 1)","6",str(p(g,c+1)))))]
