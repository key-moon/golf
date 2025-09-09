# best: 139(natte) / others: 143(4atj sisyphus luke Seek mukundan), 147(jailctf merger), 157(intgrah jimboko awu macaque sammyuri), 169(xsot ovs att joking mewheni), 267(MasukenSamba)
# ================================================================== 139 ==================================================================

import re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub("0(?=.{%d}3.{%d}3)"%((k:=sum(sum(g,[]))//21+1)*38-1,k*29-1),"8",str(p(g,c+1)))))][::-1]
# import re;p=lambda g,c=-3:g*c or[*zip(*eval(re.sub("0(?=.{%d}3.{%d}3)"%((k:=sum(sum(g,[]))//21)*38+37,k*29+28),"8",str(p(g,c+1)))))][::-1]


# import re
# def p(g):
#  k=sum(sum(g,[]))//21+1
# #  l=str(g).count("3")//7+1
#  for _ in range(4):
#   g=eval(re.sub(r"0(?=.{%d}3.{%d}3)"%(k*38-1,k*29-1),"8",str(g)))
# #   g=eval(re.sub(r"0(?=.{37}3.{28}3)","8",str(g)))
# #   g=eval(re.sub(r"0(?=.{75}3.{57}3)","8",str(g)))
# #   g=eval(re.sub(r"0(?=.{113}3.{86}3)","8",str(g)))
#   g=[*zip(*g[::-1])]
#  return g

# 2:1
# 4:1
# 8:2
# 18:3
# a//7+1

