
M = [1, 2, 3], [4, 5, 6], [7, 8, 9]
"""def soma_diagonal_principal(M):
    n = len(M)
    assert n == len(M[0])
    return sum(M[i][i] for i in range(n))"""
def soma_diagonal_principal(M):
    n=len(M)
    assert n==len(M[0])
    return sum (M [i][i]  for i in range(n))