# best: 110(ox jam) / others: 124(Code Golf International), 124(jailctf merger), 125(LogicLynx), 125(intgrah jimboko awu macaque sammyuri), 126(jacekw Potatoman nauti natte)
# =================================================== 110 ====================================================
import re;p=lambda g,c=-23:c*g or p(eval(re.sub("(?<=[24], )[^02](?=(.{%d})?, [24])"%~-len(g*3),"4",str([*zip(*g[::-1])]))),c+1)
