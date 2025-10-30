# best: 109(jailctf merger) / others: 112(intgrah jimboko awu macaque sammyuri), 113(Code Golf International), 113(4atj sisyphus luke Seek mukundan), 114(ox jam), 121(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# =================================================== 109 ===================================================
# lambda g,c=15:g*-c or[*zip(*eval(str(p(g,c-1)).replace(*["0","3, 3","3, 2","1, 2","3","2,2",a:="1,1",a][c//4::4])))][::-1]
p=lambda g,c=15:g*-c or[*zip(*eval(str(p(g,c-1)).replace(*["0","3, 3","3, 2","1, 2","3","2,2",a:="1,1",a][c//4::4])))][::-1]

# 3, 3 → 2, 2
# 2, 3 → 1, 1
# 1, 2 → 1, 1

# 2,2 -> 2
# 1,1 -> 1

#  123
#1 11X
#2 121
#3 X12
