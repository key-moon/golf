# best: 71(jailctf merger) / others: 72(4atj sisyphus luke Seek mukundan), 72(xsot ovs att joking mewheni), 82(Yuchen20), 85(kabutack), 85(jacekwl Potatoman nauti)
# ================================= 71 ================================
# lambda g:[[(c:=len({*sum(g,[])}))<3,c<2,c!=2],[0,c>1,0],[c>2,0,c==2]]
# lambda g:[[((c:=len({*sum(g,[])}))<3)*5,(c<2)*5,(c!=2)*5],[0,(c>1)*5,0],[(c>2)*5,0,(c==2)*5]]
# lambda g:[[((c:=len({*sum(g,[])}))<3)*5,(c<2)*5,c%2*5],[0,1%c*5,0],[4%c*5,0,3%c*5]]

# lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in s]for s in[[6,2,10],[0,12,0],[8,0,4]]]
# lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in b"000000000"[i-3:i]]for i in(3,6,9)]
# lambda g:[[(17314875942>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in(0,12,24)]
# lambda g:[[(69259503768>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in b"000"]
# lambda g:[[(69259503768>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in b""]
# lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in b"         "[i-3:i]]for i in(3,6,9)]
# p=lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in b"\x06\x02\x0b\x01\x0c\x01\x08\x01\x04"[i-3:i]]for i in(3,6,9)]
p=lambda g:[[(v>>len({*str(g)})-4&1)*5for v in b"\x06\x02\x0b\x01\x0c\x01\x08\x01\x04"[i-3:i]]for i in(3,6,9)]



# oox 6
# oxx 2
# oxo 10
# xxx 0
# xoo 12
# xxx 0
# xxo 8
# xxx 0
# xox 4




