# best: 77(luke, 4atj, luke/sisyphus/Seek, Seek64) / others: 79(sisyphus), 80(mukundan), 85(nauti), 85(joking+MWI), 85(joking/MWI)
# ==================================== 77 ===================================
# p=lambda g:[[(c:=len({*sum(g,[])}))<3,c<2,c!=2],[0,c>1,0],[c>2,0,c==2]]
# p=lambda g:[[((c:=len({*sum(g,[])}))<3)*5,(c<2)*5,(c!=2)*5],[0,(c>1)*5,0],[(c>2)*5,0,(c==2)*5]]
# p=lambda g:[[((c:=len({*sum(g,[])}))<3)*5,(c<2)*5,c%2*5],[0,1%c*5,0],[4%c*5,0,3%c*5]]

# p=lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in s]for s in[[6,2,10],[0,12,0],[8,0,4]]]
p=lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in b""[i-3:i]]for i in(3,6,9)]
# p=lambda g:[[(v>>len({*sum(g,[])})&1)*5for v in b"000000000"[i-3:i]]for i in(3,6,9)]
# p=lambda g:[[(17314875942>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in(0,12,24)]
# p=lambda g:[[(69259503768>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in b"000"]
# p=lambda g:[[(69259503768>>i+j+len({*sum(g,[])})&1)*5for j in(0,4,8)]for i in b""]



# [6,2,10,0,12,0,8,0,4]


# oox 6
# oxx 2
# oxo 10
# xxx 0
# xoo 12
# xxx 0
# xxo 8
# xxx 0
# xox 4
