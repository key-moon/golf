# best: 92(jailctf merger) / others: 95(Code Golf International), 95(4atj sisyphus luke Seek mukundan), 118(lv1.dev), 118(ox jam), 125(HIMAGINE THE FUTURE.)
# 141
# import re;s=re.sub;p=lambda g:(d:=s(*"21",str(g),1))and[[8-8*("2"in eval('(d:=s("[82](?=(.{%d})?.?.1)"%len(g[0]*3),"1",d)[::-1]),'*99)[98])]]

# import re;s=re.sub
# def p(g):
#  t="[82](?=(.{%d})?.?.1)"%len(g[0]*3)
#  for x in"0"*99:g=s(["2",t]["1"in g],"1",str(g),1)[::-1]
#  return[[8-8*("2"in g)]]

# 138
# import re;s=re.sub
# def p(g):
#  d=s(*"21",str(g),1)
#  for x in d:d=s("[82](?=(.{%d})?.?.1)"%len(g[0]*3),"1",d)[::-1]
#  return[[8-8*("2"in d)]]

# まじで方針が思い浮かばない。2の孤島があるので、2|8をオラクルには使えない。
# =========================================== 92 ===========================================
# p=lambda g,c=2**12:c and p([(l:=0)or[l:=v and(v|l|((v<3)and(c:=c//2)))for v in s]for s in zip(*g[::-1])],c-1)or[[8*("9"in str(g))]]
# p=lambda g,c=4**6:c and p([(l:=0)or[l:=v and(v|l|(v<3and(c:=c//2)))for v in s]for s in zip(*g[::-1])],c-1)or[[8*("9"in str(g))]]
p=lambda g,c=4**6:-c*[[8*("9"in str(g))]]or p([(l:=0)or[l:=v and(v|l|(v<3and(c:=c//2)))for v in s]for s in zip(*g[::-1])],c-1)
