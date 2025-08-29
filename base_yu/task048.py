# best: 98(4atj sisyphus luke Seek, 4atj) / others: 126(luke/sisyphus/Seek), 126(Seek64), 127(sisyphus), 131(duckyluuk), 136(joking+MWI)
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

# まじで方針が思い浮かばない、99だったら一個だけ置換 / 
# ============================================== 98 ==============================================
# lambda g,c=32:c and p([(l:=0)or[l:=v&(c>>4)and(c:=16)or v and(v|l)for v in s]for s in zip(*g[::-1])],c-1)or[[8-8*("6"in str(g))]]
p=lambda g,c=64:c and p([(l:=0)or[l:=(v&(c>>5))and(c:=32)//32or v and min(v,l)for v in s]for s in zip(*DUMP(g)[::-1])],c-1)or[[8-8*("2"in str(g))]]
