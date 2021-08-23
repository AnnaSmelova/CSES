'''
8. Two Sets
Time limit: 1.00 s Memory limit: 512 MB
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input

The only input line contains an integer n.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets.
First, print the number of elements in the first set followed by the elements themselves
in a separate line, and then, print the second set in a similar way.

Constraints
1≤n≤106
Example 1

Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6

Example 2

Input:
6

Output:
NO
'''


def solution_8():
    n = int(input())
    s = (1 + n) * n / 2
    if s % 2 == 1:
        print('NO')
    else:
        print('YES')
        lst = list(range(1, n+1))
        big_ind_cnt = n // 4
        small_ind_cnt = big_ind_cnt - 1
        big = lst[n - big_ind_cnt:]
        sm = lst[:small_ind_cnt]
        cur_sum = sum(big) + sum(sm)
        if cur_sum < s / 2:
            sm.append(lst[small_ind_cnt])
            cur_sum += lst[small_ind_cnt]
        if cur_sum < s / 2:
            big.append(lst[n - big_ind_cnt - 1])
            cur_sum += lst[n - big_ind_cnt - 1]
        if cur_sum == s / 2:
            first = big + sm
            print(len(first))
            print(' '.join(list(map(str,first))))
            second = list(set(lst) - set(first))
            print(len(second))
            print(' '.join(list(map(str, second))))

solution_8()

