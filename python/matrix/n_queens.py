import ipdb


# Queens can't be placed where they can attack each other.
# We need to know the current column and the positive and
# negative diagonals:
#
#    neg_diag = (r - c)
#    pos_diag = (r + c)
#
# We can then backtrack.

def nqueens(n):
    board = [["."] * n for _ in range(n)]
    res = []

    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r - c) in neg_diag or (r + c) in pos_diag:
                continue

            board[r][c] = "Q"
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            backtrack(r + 1)

            board[r][c] = "."
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return res


print(nqueens(4))
