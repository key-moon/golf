# best: 46(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, adakoda) / others: 50(intgrah jimboko awu macaque sammyuri), 52(ox jam), 54(cubbus), 54(Tony Li), 54(Tony Li & Darren Amadeus Martin)
# ==================== 46 ====================
# p=lambda g:[[v and g[6][0]for v in s]for s in g[:6]+g[:1]]
p=lambda g:[[0]+[v and g[6][0]for v in s[1:]]for s in g]
# p=lambda g:[[(v>0)*g[6][0]for v in s]for s in g[:6]+g[:1]]
