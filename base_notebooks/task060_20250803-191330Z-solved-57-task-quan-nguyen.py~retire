def p(g):
        res = [list(r) for r in g]
        h, w = len(g), len(g[0])
        for r in range(h):
            pts = [(c, g[r][c]) for c in range(w) if g[r][c] != 0]
            if len(pts) == 2:
                (c1, v1), (c2, v2) = pts
                mid = (c1 + c2) // 2
                for i in range(c1 + 1, mid): res[r][i] = v1
                res[r][mid] = 5
                for i in range(mid + 1, c2): res[r][i] = v2
        return res
    