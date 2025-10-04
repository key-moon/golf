# best: 125(jailctf merger) / others: 126(jacekw Potatoman nauti natte), 126(4atj sisyphus luke Seek mukundan), 126(natte), 126(ox jam), 171(intgrah jimboko awu macaque sammyuri)
# =========================================================== 125 ===========================================================
import re;p=lambda g,c=-23:c*g or p(eval(re.sub("(?<=[24], )[^02](?=(.{%d})?, [24])"%~-len(g*3),"4",str([*zip(*g[::-1])]))),c+1)
