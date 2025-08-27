# best: 98(4atj sisyphus luke Seek, 4atj) / others: 126(luke/sisyphus/Seek), 126(Seek64), 127(sisyphus), 131(duckyluuk), 136(joking+MWI)
# ============================================== 98 ==============================================
import re;s=re.sub
def p(g):
 d=s(*"21",s("[[ ,]","",str(g)),1)
 for x in d:d=s(f"[82](?=({'.'*len(g[0])})?1)","1",d)[::-1]
 return[[8-8*("2"in d)]]
