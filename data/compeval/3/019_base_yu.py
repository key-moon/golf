# best: 119(mukundan, jailctf merger) / others: 126(xsot ovs att joking mewheni), 128(4atj sisyphus luke Seek), 130(duckyluuk), 141(biz), 152(natte)
# ======================================================== 119 ========================================================
# p=lambda g,z=[0]*9:[[v or any([0,*[z,*g*2,z][i+(k&2)]*2,0][j+k%2*2]for k in range(4))*8for j,v in enumerate(s*2)]for i,s in enumerate(g*2)]
# p=lambda g,c=-1,l=[]:c*[s*2for s in g*2]or[l:=[v or any({*[0,*l][i:i+3:2]}-{8})*8for i,v in enumerate(s)]for s in p(g,c+1)[::-1]]
# p=lambda g,c=-1,l=[]:c*[s*2for s in g*2]or[(l:=[0,0]+[v+(v<1)*any({*(l:=l[1:])[:3:2]}-{8})*8for v in s])[2:]for s in p(g,c+1)[::-1]]
# p=lambda g,c=-1,l=[]:c*g*2or[l:=[v or any({*[0,*l][i:i+3:2]}-{8})*8for i,v in enumerate(s*(c+2))]for s in p(g,c+1)[::-1]]
p=lambda g,c=-2,l=[]:c*g or[l:=[v or any({*[0,*l][i:i+3:2]}-{8})*8for i,v in enumerate(~c%3*s)]for s in p(g,c+2)[::-1]]
