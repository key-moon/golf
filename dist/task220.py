def p(g):
 AE={3:6,8:4,2:1}
 for AC,AF in enumerate(g):
  for AD,AG in enumerate(AF):
   if AG in AE:
    for AA in(-1,0,1):
     for AB in(-1,0,1):
      if AA or AB:
       g[AC+AA][AD+AB]=AE[AG]
 return g