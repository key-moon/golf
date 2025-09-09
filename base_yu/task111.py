# best: 60(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 61(jonas ryno kg583), 61(JRK), 68(MasukenSamba), 73(kabutack), 75(natte)
# =========================== 60 ===========================
# lambda g:(u:=sum(g,[]).index(5))and[g[u//10+1+i][u%10-1:u%10+2]for i in range(3)]
# lambda g:(u:=sum(g,[]).index(5))and[g[u//10+i][u%10-1:][:3]for i in range(1,4)]
# lambda g:(u:=sum(g,[]).index(5))and[s[u%10-1:][:3]for s in g[u//10+1:][:3]]
# lambda g:(u:=(G:=sum(g,[])).index(5))and[G[u+9:u+12],G[u+19:u+22],G[u+29:u+32]]
# lambda g:(u:=(G:=sum(g,[])).index(5))and[G[u+9+i*10:][:3]for i in range(3)]
# lambda g:[[*iter(sum(g,[]).pop,5)][::-1][8+i*10:][:3]for i in range(3)]
# lambda g:[[*iter(sum(g,[]).pop,5)][1-i*10::-1][:3]for i in(1,2,3)]
# lambda g:[[*iter(sum(g,g).pop,5)][-i::-1][:3]for i in(9,19,29)]
# lambda g:[[*iter(sum(g,g).pop,5)][3-i:-i:-1]for i in(12,22,32)]
# lambda g:[[*iter(sum(g,g).pop,5)][3-i:-i:-1]for i in b"123"]
p=lambda g:[[*iter(sum(g,g).pop,5)][3-i:-i:-1]for i in b"\x0c\x16\x20"]



