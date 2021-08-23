'''
7. Two Knights
Time limit: 1.00 s Memory limit: 512 MB
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard
so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints
1≤n≤10000
Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848
'''


def get_bad_points_count(n):
    if n == 1:
        return 0
    elif n == 2:
        return 6
    elif n == 3:
        return 28
    elif n == 4:
        return 96
    else:
        return int((n**4 - n**2 - 8 * (n - 4)**2 - 40 * (n - 4) - 48) / 2)


def solution_7():
    n = int(input())
    for k in range(1, n + 1):
        print(get_bad_points_count(k))


solution_7()

