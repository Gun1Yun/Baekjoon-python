# 행렬
import sys
In = sys.stdin.readline


def check_same(mat1, mat2):
    for idx in range(len(mat1)):
        if mat1[idx] != mat2[idx]:
            return False

    return True


def reverse_submat(mat, row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            if mat[i][j] == '0':
                mat[i][j] = '1'
            else:
                mat[i][j] = '0'


def main():
    n, m = map(int, In().split())
    mat_a = []
    mat_b = []

    for r in range(n*2):
        sub = list(map(str, In().rstrip()))
        if r < n:
            mat_a.append(sub)
        else:
            mat_b.append(sub)

    cnt = 0

    for i in range(n):
        for j in range(m):
            if mat_a[i][j] != mat_b[i][j]:
                if i+3 <= n and j+3 <= m:
                    reverse_submat(mat_a, i, j)
                    cnt += 1
                    if check_same(mat_a, mat_b):
                        break

    if check_same(mat_a, mat_b):
        print(cnt)
    else:
        print(-1)


if __name__ == "__main__":
    main()
