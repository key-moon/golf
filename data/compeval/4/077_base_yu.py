# best: 126(4atj sisyphus luke Seek, jailctf merger) / others: 127(mukundan), 152(xsot ovs att joking mewheni), 198(Jonas), 225(MasukenSamba), 242(Afordancja)
# =========================================================== 126 ============================================================
import re;p=lambda g,c=-23:c*g or p(eval(re.sub(r"(?<=[24], )[^02](?=(.{%d})?, [24])"%~-len(g*3),"4",str([*zip(*g[::-1])]))),c+1)
