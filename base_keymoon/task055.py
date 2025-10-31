# best: 77(ox jam) / others: 79(Code Golf International), 79(jailctf merger), 82(LogicLynx), 83(4atj sisyphus luke Seek mukundan), 83(FuunAgent)
# lambda g,i=0:[[c or b"\0\2\0\4\6\3\0\1\0"[j]for c in r if(j:=j+(c==8))+1]for r in g if(i:=i+6-len({*r})*3,j:=i)]
# ==================================== 77 ===================================
# lambda g,i=0:[[c or b"x020463010"[j]&7for c in r if(j:=j+(c>0))+1]for r in g if(i:=i+r[0]//8*3,j:=i)]
# lambda g,i=1:[[c or b"x020463010"[j]&7for c in r if(j:=j+(c>0))]for r in g if(i:=i+r[0]//8*3,j:=i)]
# lambda g,i=0:[(i:=i+r[0]//8*3,j:=i)and[c and(j:=j+1)-j+8or b"020463010"[j]&7for c in r]for r in g]
# lambda g,i=0:[(i:=i+r[0]//8*3,j:=i)and[c and(j:=j+1)-j+8or 2222096>>j*3&7for c in r]for r in g]
# lambda g,i=0:[(i:=i+r[0]//2,j:=i)and[c and(j:=j+1)-j+8or 0x80f4010>>j*3&7for c in r]for r in g]
# lambda g,i=0:[(i:=i+r[0]//2,j:=i)and[[8,0x80f4010>>(j:=j+(c>0))*3&7][c<1]for c in r]for r in g]
# lambda g,i=0:[(i:=i+r[0],j:=i)and[c or 586768>>j&7for c in r if(j:=j+c//8*3)|1]for r in g]
# lambda g,i=1:[(i:=i+r[0],j:=i)and[c or 1173536>>j&7for c in r if(j:=j+c//8*3)]for r in g]
# lambda g,i=1:[(i:=i+r[0],j:=i)and[c+146692*(8-c)>>j&7for c in r if(j:=j+c//8*3)]for r in g]
# lambda g,i=0:[(i:=i+r[0],j:=i)and[[586768>>(j:=j+c//8*3)&7,c][c>0]for c in r]for r in g]
p=lambda g,i=0:[(i:=i+r[0],j:=i)and[c and(j:=j+3)%1+8or 586768>>j&7for c in r]for r in g]


# 
# 0b000_001_000_011_110_100_000_010_000
# 0b000_001_000_11_110_100_00_010_000
# sum([(c&7) << (i*3) for i, c in enumerate(b"02004630010")])
