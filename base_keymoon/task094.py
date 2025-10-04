# best: 98(jailctf merger) / others: 102(4atj sisyphus luke Seek mukundan), 106(ox jam), 116(jacekw Potatoman nauti natte), 116(jacekw Potatoman nauti), 116(intgrah jimboko awu macaque sammyuri)
# ============================================== 98 ==============================================
# port re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub(r"8(?=[^(]+\(.{,40}1.{43}1, 1)","6",str(p(g,c+1)))))]
import re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub(r"8(?=[^(]*\([^(]*1.{43}1, 1)","6",str(p(g,c+1)))))]
