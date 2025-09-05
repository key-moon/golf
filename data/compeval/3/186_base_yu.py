# best: 62(luke, 4atj, luke/sisyphus/Seek, Seek64) / others: 63(mukundan), 66(joking+MWI), 66(joking/MWI), 66(joking), 66(xsot)
# ============================ 62 ============================
# p=lambda g:[[((c:=sum(sum(g,[])))>0)*2,(c>1)*2,(c>2)*2],[0,(c>3)*2,0],[0,0,0]]
# p=lambda g:[([2]*(c:=sum(sum(g,[])))+[0]*2)[:3],[0,(c>3)*2,0],[0,0,0]]
# p=lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0,*u[3:5]],[0,0,0]]
# p=lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0,*u[3:5]],u[-3:]]
p=lambda g:[(u:=[2]*sum(sum(g,[]))+[0]*9)[:3],[0]+u[3:5],u[-3:]]