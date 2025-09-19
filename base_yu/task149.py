# best: 75(jailctf merger) / others: 77(4atj sisyphus luke Seek mukundan), 79(ox jam), 79(xsot ovs att joking mewheni), 80(natte), 80(Yuchen20)
# =================================== 75 ==================================

# p=lambda g,R=range(3):[[sum(sum(g[i*4+k][j*4:j*4+3])for k in R)//9for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(sum(g[i+k][j:j+3])for k in(0,1,2))//9for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(sum(s[j:j+3])for s in g[i:i+3])//9for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(g[i][j:j+3]+g[i+1][j:j+3]+g[i+2][j:j+3])//9for j in R]for i in R]
# lambda g,R=b"37b":[[sum(sum(s[j-3:j])for s in g[i-3:i])//9for j in R]for i in R]
p=lambda g,R=b"\x03\x07\x0b":[[sum(sum(s[j-3:j])for s in g[i-3:i])//9for j in R]for i in R]

# def p(g):
#  u=[*eval("[0]*3,"*3)]
#  for i in range(11):
#   for j in range(11):
#    u[i//4][j//4]+=g[i][j]==6
#  return[[v//2 for v in s]for s in u]
