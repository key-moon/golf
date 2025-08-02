def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def p(I):I=tuple(map(tuple,I));A=val_func_rot180(I);return[*map(list,A)]