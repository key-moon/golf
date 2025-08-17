from arc_types import *


def identity(x):
    return x


def add(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)


def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)


def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def divide(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)


def invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])


def even(n):
    return n % 2 == 0


def double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)


def halve(n):
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)


def flip(b):
    return not b


def equality(a, b):
    return a == b


def contained(A, B):
    return A in B


def combine(a, b):
    return type(a)((*a, *b))


def intersection(a, b):
    return a & b


def difference(a, b):
    return type(a)(e for e in a if e not in b)


def dedupe(A):
    return tuple(e for i, e in enumerate(A) if A.index(e) == i)


def order(A, B):
    return tuple(sorted(A, key=B))


def repeat(A, B):
    return tuple(A for i in range(B))


def greater(a, b):
    return a > b


def size(A):
    return len(A)


def merge(A):
    return type(A)(e for c in A for e in c)


def maximum(A):
    return max(A, default=0)


def minimum(Aa):
    return min(Aa, default=0)


def valmax(A, B):
    return B(max(A, key=B, default=0))


def valmin(A, B):
    return B(min(A, key=B, default=0))


def argmax(A, B):
    return max(A, key=B)


def argmin(A, B):
    return min(A, key=B)


def mostcommon(A):
    return max(set(A), key=A.count)


def leastcommon(A):
    return min(set(A), key=A.count)


def initset(A):
    return frozenset({A})


def both(a, b):
    return a and b


def either(a, b):
    return a or b


def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)


def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)


def crement(x):
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1))


def sign(x):
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (0 if x[0] == 0 else (1 if x[0] > 0 else -1),        0 if x[1] == 0 else (1 if x[1] > 0 else -1))


def positive(x):
    return x > 0


def toivec(i):
    return (i, 0)


def tojvec(j):
    return (0, j)


def sfilter(A, B):
    return type(A)(e for e in A if B(e))


def mfilter(A, B):
    return merge(sfilter(A, B))


def extract(A, B):
    return next(e for e in A if B(e))


def totuple(A):
    return tuple(A)


def first(A):
    return next(iter(A))


def last(A):
    return max(enumerate(A))[1]


def insert(A, B):
    return B.union(frozenset({A}))


def remove(A, B):
    return type(B)(e for e in B if e != A)


def other(A, B):
    return first(remove(B, A))


def interval(A, B, C):
    return tuple(range(A, B, C))


def astuple(a, b):
    return (a, b)


def product(a, b):
    return frozenset((i, j) for j in b for i in a)


def pair(a, b):
    return tuple(zip(a, b))


def branch(A, a, b):
    return a if A else b


def compose(A, B):
    return lambda x: A(B(x))


def chain(h, g, f,):
    return lambda x: h(g(f(x)))


def matcher(A, B):
    return lambda x: A(x) == B


def rbind(A, B):
    n = A.__code__.co_argcount
    if n == 2:
        return lambda x: A(x, B)
    elif n == 3:
        return lambda x, y: A(x, y, B)
    else:
        return lambda x, y, z: A(x, y, z, B)


def lbind(A, B):
    n = A.__code__.co_argcount
    if n == 2:
        return lambda y: A(B, y)
    elif n == 3:
        return lambda y, z: A(B, y, z)
    else:
        return lambda y, z, a: A(B, y, z, a)


def power(A, n):
    if n == 1:
        return A
    return compose(A, power(A, n - 1))


def fork(A, a, b):
    return lambda x: A(a(x), b(x))


def apply(A, B):
    return type(B)(A(e) for e in B)


def rapply(A, B):
    return type(A)(function(B) for function in A)


def mapply(A, B):
    return merge(apply(A, B))


def papply(A, a, b):
    return tuple(A(i, j) for i, j in zip(a, b))


def mpapply(A, a, b):
    return merge(papply(A, a, b))


def prapply(A, a, b):
    return frozenset(A(i, j) for j in b for i in a)


def mostcolor(A):
    values = [v for r in A for v in r] if isinstance(A, tuple) else [v for v, _ in A]
    return max(set(values), key=values.count)
    

def leastcolor(A):
    values = [v for r in A for v in r] if isinstance(A, tuple) else [v for v, _ in A]
    return min(set(values), key=values.count)


def height(A):
    if len(A) == 0:
        return 0
    if isinstance(A, tuple):
        return len(A)
    return lowermost(A) - uppermost(A) + 1


def width(A):
    if len(A) == 0:
        return 0
    if isinstance(A, tuple):
        return len(A[0])
    return rightmost(A) - leftmost(A) + 1


def shape(A):
    return (height(A), width(A))


def portrait(A):
    return height(A) > width(A)


def colorcount(A, B):
    if isinstance(A, tuple):
        return sum(row.count(B) for row in A)
    return sum(v == B for v, _ in A)


def colorfilter(A, B):
    return frozenset(obj for obj in A if next(iter(obj))[0] == B)


def sizefilter(A, n):
    return frozenset(item for item in A if len(item) == n)


def asindices(A):
    return frozenset((i, j) for i in range(len(A)) for j in range(len(A[0])))


def ofcolor(A, B):
    return frozenset((i, j) for i, r in enumerate(A) for j, v in enumerate(r) if v == B)


def ulcorner(A):
    return tuple(map(min, zip(*toindices(A))))


def urcorner(A):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(A)))))


def llcorner(A):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(A)))))


def lrcorner(A):
    return tuple(map(max, zip(*toindices(A))))


def crop(A, B, C):
    return tuple(r[B[1]:B[1]+C[1]] for r in A[B[0]:B[0]+C[0]])


def toindices(A):
    if len(A) == 0:
        return frozenset()
    if isinstance(next(iter(A))[1], tuple):
        return frozenset(index for value, index in A)
    return A


def recolor(A, B):
    return frozenset((A, index) for index in toindices(B))


def shift(A, C):
    if len(A) == 0:
        return A
    di, dj = C
    if isinstance(next(iter(A))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in A)
    return frozenset((i + di, j + dj) for i, j in A)


def normalize(A):
    if len(A) == 0:
        return A
    return shift(A, (-uppermost(A), -leftmost(A)))


def dneighbors(A):
    return frozenset({(A[0] - 1, A[1]), (A[0] + 1, A[1]), (A[0], A[1] - 1), (A[0], A[1] + 1)})


def ineighbors(A):
    return frozenset({(A[0] - 1, A[1] - 1), (A[0] - 1, A[1] + 1), (A[0] + 1, A[1] - 1), (A[0] + 1, A[1] + 1)})


def neighbors(A):
    return dneighbors(A) | ineighbors(A)


def objects(A, B, C, D):
    bg = mostcolor(A) if D else None
    objs = set()
    occupied = set()
    h, w = len(A), len(A[0])
    unvisited = asindices(A)
    diagfun = neighbors if C else dneighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = A[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = A[cand[0]][cand[1]]
                if (val == v) if B else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)


def partition(A):
    return frozenset(frozenset((v, (i, j)) for i, r in enumerate(A) for j, v in enumerate(r) if v == value) for value in palette(A))


def fgpartition(A):
    return frozenset(       frozenset(           (v, (i, j)) for i, r in enumerate(A) for j, v in enumerate(r) if v == value
        ) for value in palette(A) - {mostcolor(A)}
    )


def uppermost(A):
    return min(i for i, j in toindices(A))


def lowermost(A):
    return max(i for i, j in toindices(A))


def leftmost(A):
    return min(j for i, j in toindices(A))


def rightmost(A):
    return max(j for i, j in toindices(A))


def square(A):
    return len(A) == len(A[0]) if isinstance(A, tuple) else height(A) * width(A) == len(A) and height(A) == width(A)


def vline(A):
    return height(A) == len(A) and width(A) == 1


def hline(A):
    return width(A) == len(A) and height(A) == 1


def hmatching(a, b):
    return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0


def vmatching(a, b):
    return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0


def manhattan(a, b):
    return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))


def adjacent(a, b):
    return manhattan(a, b) == 1


def bordering(A, B):
    return uppermost(A) == 0 or leftmost(A) == 0 or lowermost(A) == len(B) - 1 or rightmost(A) == len(B[0]) - 1


def centerofmass(A):
    return tuple(map(lambda x: sum(x) // len(A), zip(*toindices(A))))


def palette(A):
    if isinstance(A, tuple):
        return frozenset({v for r in A for v in r})
    return frozenset({v for v, _ in A})


def numcolors(A):
    return len(palette(A))


def color(A):
    return next(iter(A))[0]


def toobject(A, B):
    h, w = len(B), len(B[0])
    return frozenset((B[i][j], (i, j)) for i, j in toindices(A) if 0 <= i < h and 0 <= j < w)


def asobject(A):
    return frozenset((v, (i, j)) for i, r in enumerate(A) for j, v in enumerate(r))


def rot90(A):
    return tuple(row for row in zip(*A[::-1]))


def rot180(A):
    return tuple(tuple(row[::-1]) for row in A[::-1])


def rot270(A):
    return tuple(tuple(row[::-1]) for row in zip(*A[::-1]))[::-1]


def hmirror(A):
    if isinstance(A, tuple):
        return A[::-1]
    d = ulcorner(A)[0] + lrcorner(A)[0]
    if isinstance(next(iter(A))[1], tuple):
        return frozenset((v, (d - i, j)) for v, (i, j) in A)
    return frozenset((d - i, j) for i, j in A)


def vmirror(A):
    if isinstance(A, tuple):
        return tuple(row[::-1] for row in A)
    d = ulcorner(A)[1] + lrcorner(A)[1]
    if isinstance(next(iter(A))[1], tuple):
        return frozenset((v, (i, d - j)) for v, (i, j) in A)
    return frozenset((i, d - j) for i, j in A)


def dmirror(A):
    if isinstance(A, tuple):
        return tuple(zip(*A))
    a, b = ulcorner(A)
    if isinstance(next(iter(A))[1], tuple):
        return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in A)
    return frozenset((j - b + a, i - a + b) for i, j in A)


def cmirror(A):
    if isinstance(A, tuple):
        return tuple(zip(*(r[::-1] for r in A[::-1])))
    return vmirror(dmirror(vmirror(A)))


def fill(A, B, C):
    h, w = len(A), len(A[0])
    grid_filled = list(list(row) for row in A)
    for i, j in toindices(C):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = B
    return tuple(tuple(row) for row in grid_filled)


def paint(A, B):
    h, w = len(A), len(A[0])
    grid_painted = list(list(row) for row in A)
    for value, (i, j) in B:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple(tuple(row) for row in grid_painted)


def underfill(A, B, C):
    h, w = len(A), len(A[0])
    bg = mostcolor(A)
    g = list(list(r) for r in A)
    for i, j in toindices(C):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = B
    return tuple(tuple(r) for r in g)


def underpaint(A, B):
    h, w = len(A), len(A[0])
    bg = mostcolor(A)
    g = list(list(r) for r in A)
    for value, (i, j) in B:
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple(tuple(r) for r in g)


def hupscale(A, B):
    g = tuple()
    for row in A:
        r = tuple()
        for value in row:
            r = r + tuple(value for num in range(B))
        g = g + (r,)
    return g


def vupscale(A, B):
    g = tuple()
    for row in A:
        g = g + tuple(row for num in range(B))
    return g


def upscale(A, B):
    if isinstance(A, tuple):
        g = tuple()
        for row in A:
            upscaled_row = tuple()
            for value in row:
                upscaled_row = upscaled_row + tuple(value for num in range(B))
            g = g + tuple(upscaled_row for num in range(B))
        return g
    else:
        if len(A) == 0:
            return frozenset()
        di_inv, dj_inv = ulcorner(A)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = shift(A, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
            for io in range(B):
                for jo in range(B):
                    o.add((value, (i * B + io, j * B + jo)))
        return shift(frozenset(o), (di_inv, dj_inv))


def downscale(A, B):
    h, w = len(A), len(A[0])
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % B == 0:
                r = r + (A[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % B == 0:
            dsg = dsg + (g[i],)
    return dsg


def hconcat(a, b):
    return tuple(i + j for i, j in zip(a, b))


def vconcat(a, b):
    return a + b


def subgrid(A, B):
    return crop(B, ulcorner(A), shape(A))


def hsplit(A, n):
    h, w = len(A), len(A[0]) // n
    offset = len(A[0]) % n != 0
    return tuple(crop(A, (0, w * i + i * offset), (h, w)) for i in range(n))


def vsplit(A, n):
    h, w = len(A) // n, len(A[0])
    offset = len(A) % n != 0
    return tuple(crop(A, (h * i + i * offset, 0), (h, w)) for i in range(n))


def cellwise(a, b, A):
    h, w = len(a), len(a[0])
    resulting_grid = tuple()
    for i in range(h):
        row = tuple()
        for j in range(w):
            a_value = a[i][j]
            value = a_value if a_value == b[i][j] else A
            row = row + (value,)
        resulting_grid = resulting_grid + (row, )
    return resulting_grid


def replace(A, B, C):
    return tuple(tuple(C if v == B else v for v in r) for r in A)


def switch(A, a, b):
    return tuple(tuple(v if (v != a and v != b) else {a: b, b: a}[v] for v in r) for r in A)


def center(A):
    return (uppermost(A) + height(A) // 2, leftmost(A) + width(A) // 2)


def position(a, b):
    ia, ja = center(toindices(a))
    ib, jb = center(toindices(b))
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    elif ja == jb:
        return (1 if ia < ib else -1, 0)
    elif ia < ib:
        return (1, 1 if ja < jb else -1)
    elif ia > ib:
        return (-1, 1 if ja < jb else -1)


def index(A, B):
    i, j = B
    h, w = len(A), len(A[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return A[B[0]][B[1]] 


def canvas(A, B):
    return tuple(tuple(A for j in range(B[1])) for i in range(B[0]))


def corners(A):
    return frozenset({ulcorner(A), urcorner(A), llcorner(A), lrcorner(A)})


def connect(a, b):
    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()


def cover(A, B):
    return fill(A, mostcolor(A), toindices(B))


def trim(A):
    return tuple(r[1:-1] for r in A[1:-1])


def move(A, B, C):
    return paint(cover(A, B), shift(B, C))


def tophalf(A):
    return A[:len(A) // 2]


def bottomhalf(A):
    return A[len(A) // 2 + len(A) % 2:]


def lefthalf(A):
    return rot270(tophalf(rot90(A)))


def righthalf(A):
    return rot270(bottomhalf(rot90(A)))


def vfrontier(A):
    return frozenset((i, A[1]) for i in range(30))


def hfrontier(A):
    return frozenset((A[0], j) for j in range(30))


def backdrop(A):
    if len(A) == 0:
        return frozenset({})
    indices = toindices(A)
    si, sj = ulcorner(indices)
    ei, ej = lrcorner(A)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))


def delta(B):
    if len(B) == 0:
        return frozenset({})
    return backdrop(B) - toindices(B)


def gravitate(A, B):
    si, sj = center(A)
    di, dj = center(B)
    i, j = 0, 0
    if vmatching(A, B):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = i, j
    c = 0
    while not adjacent(A, B) and c < 42:
        c += 1
        gi += i
        gj += j
        A = shift(A, (i, j))
    return (gi - i, gj - j)


def inbox(A):
    ai, aj = uppermost(A) + 1, leftmost(A) + 1
    bi, bj = lowermost(A) - 1, rightmost(A) - 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def outbox(A):
    ai, aj = uppermost(A) - 1, leftmost(A) - 1
    bi, bj = lowermost(A) + 1, rightmost(A) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def box(A):
    if len(A) == 0:
        return A
    ai, aj = ulcorner(A)
    bi, bj = lrcorner(A)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def shoot(A, B):
    return connect(A, (A[0] + 42 * B[0], A[1] + 42 * B[1]))


def occurrences(A, B):
    occs = set()
    normed = normalize(B)
    h, w = len(A), len(A[0])
    oh, ow = shape(B)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = T
            for v, (a, b) in shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and A[a][b] == v):
                    occurs = F
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)


def frontiers(A):
    h, w = len(A), len(A[0])
    row_indices = tuple(i for i, r in enumerate(A) if len(set(r)) == 1)
    column_indices = tuple(j for j, c in enumerate(dmirror(A)) if len(set(c)) == 1)
    hfrontiers = frozenset({frozenset({(A[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(A[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers


def compress(A):
    ri = tuple(i for i, r in enumerate(A) if len(set(r)) == 1)
    ci = tuple(j for j, c in enumerate(dmirror(A)) if len(set(c)) == 1)
    return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(A) if i not in ri)


def hperiod(A):
    normalized = normalize(A)
    w = width(normalized)
    for p in range(1, w):
        offsetted = shift(normalized, (0, -p))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if j >= 0})
        if pruned.issubset(normalized):
            return p
    return w


def vperiod(A):
    normalized = normalize(A)
    h = height(normalized)
    for p in range(1, h):
        offsetted = shift(normalized, (-p, 0))
        pruned = frozenset({(c, (i, j)) for c, (i, j) in offsetted if i >= 0})
        if pruned.issubset(normalized):
            return p
    return h