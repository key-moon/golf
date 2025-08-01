def p(val_g):
    val_h=[val_R[:]for val_R in val_g]
    val_z=[(val_I,val_J)
           for val_I in range(len(val_g))
           for val_J in range(len(val_g[0]))
           if val_g[val_I][val_J]==3]
    val_r0=min(val_I for val_I,val_J in val_z)
    val_r1=max(val_I for val_I,val_J in val_z)
    val_c0=min(val_J for val_I,val_J in val_z)
    val_c1=max(val_J for val_I,val_J in val_z)
    val_t=[(val_I,val_J,
            val_r0+val_J-val_c0,
            val_c1+val_r0-val_I)
           for val_I in range(val_r0,val_r1+1)
           for val_J in range(val_c0,val_c1+1)
           if val_g[val_I][val_J]==2]
    [ val_h[val_I].__setitem__(val_J,0)
      or
      val_h[val_K].__setitem__(val_L,2)
      for val_I,val_J,val_K,val_L in val_t ]
    return val_h
