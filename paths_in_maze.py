from collections import deque


def maze(matrix):
    n = 3
    m = 4
    q = deque()

    q.append((0, 0))
    count = 0

    while len(q) > 0:
        p = q.popleft()

        if p[0] == n - 1 and p[1] == m - 1:
            count += 1

        if p[0] + 1 < n and matrix[p[0] + 1][p[1]] == 1:
            q.append((p[0] + 1, p[1]))

        if p[1] + 1 < m and matrix[p[0]][p[1] + 1] == 1:
            q.append((p[0] + 1, p[1]))
    return count
