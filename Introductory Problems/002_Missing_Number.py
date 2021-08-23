'''
2. Missing Number
Time limit: 1.00 s Memory limit: 512 MB
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
2≤n≤2⋅105
Example

Input:
5
2 3 1 5

Output:
4
'''

def solution_2():
    n = int(input())
    nums = map(int, input().split(' '))
    n_nums = range(1,n+1)
    print(list((set(n_nums) - set(nums)))[0])

solution_2()

