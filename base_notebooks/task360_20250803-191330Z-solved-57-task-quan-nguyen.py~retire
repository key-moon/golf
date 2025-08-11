def p(g):
        w = len(g[0])
        sep_c = next(c for c in range(w) if all(g[r][c] == g[0][c] for r in range(len(g))) and g[0][c] != 0)
        
        left = [row[:sep_c] for row in g]
        right_flipped = [row[sep_c+1:][::-1] for row in g]
        
        return [[(l if l != 0 else r) for l, r in zip(l_row, r_row)] 
                for l_row, r_row in zip(left, right_flipped)]
    