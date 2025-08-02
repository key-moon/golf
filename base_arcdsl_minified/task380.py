def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def p(I):I=tuple(map(tuple,I));A=val_func_rot270(I);return[*map(list,A)]