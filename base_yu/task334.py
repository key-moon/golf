# best: 66(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 69(ox jam), 75(xsot ovs att joking mewheni), 76(jacekw Potatoman nauti), 76(jacekwl Potatoman nauti), 78(intgrah jimboko awu macaque sammyuri)
# ============================== 66 ==============================
# p=lambda g:[[[0,5,0],[5,5,5],[0,5,0]],[[5,5,5],[0,5,0],[0,5,0]],[[0,0,5],[0,0,5],[5,5,5]]][max(sum(g,[]))-1]
# p=lambda g:[[*b"050550055"[u:=max(sum(g,[]))::3]],[*b"500550505"[u::3]],[*b"005555005"[u::3]]]
# p=lambda g:[(u:=[*b"_500505550005505055050555050"[max(sum(g,[]))::3]])[:3],u[3:6],u[6:]]
# p=lambda g:[(u:=[int(c)*5for c in bin(181299833)[max(sum(g,[]))+2::3]])[:3],u[3:6],u[6:]]
# p=lambda g:(a:=[0,5,0],b:=[5,5,5],c:=[0,0,5])and[[a,b,a],[b,a,a],[c,c,b]][max(sum(g,[]))-1]
# p=lambda g:[[a:=[0,5,0],b:=[5,5,5],a],[b,a,a],[[0,0,5]]*2+[b]][max(sum(g,[]))-1]
# p=lambda g:[[a:=[0,5,0],b:=[5,5,5],a],[b,a,a],[[0,0,5]]*2+[b]][max(sum(g,[]))-1]
p=lambda g:[a:=[0,5,0],b:=[5,5,5],c:=[0,0,5],b,a,c,a,a,b][max(sum(g,[]))-1::3]
# p=lambda g:[(a:=[[0,5,0],[5,5,5]]*2)[:3],a[1:3]+a[:1],[[0,0,5]]*2+a[1:2]][max(sum(g,[]))-1]

# aba,baa,ccb
# abcbacaab

# 050555050
# 555050050
# 005005555



# 1
# .#.
# ###
# .#.

# 2
# ###
# .#.
# .#.

# 3
# ..#
# ..#
# ###
