from cell import Cell
n = 3
m = 3
mat = [[Cell(i, j) for j in range(m)] for i in range(n)]

mat[0][1].alive = True
mat[1][0].alive = True
mat[1][1].alive = True

for k in mat:
    print(' '.join(['1' if l.alive else '0' for l in k]))
print()

for row in mat:
    for col in row:
        col.discover(mat, n, m)

for r in mat:
    for c in r:
        c.cycle()

print()
for k in mat:
    print(' '.join(['1' if l.alive else '0' for l in k]))



