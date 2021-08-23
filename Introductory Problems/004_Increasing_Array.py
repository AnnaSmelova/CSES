'''
4. Increasing Array
You are given an array of n integers. You want to modify the array so that it is increasing,
i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input

The first input line contains an integer n: the size of the array.

Then, the second line contains n integers x1,x2,…,xn: the contents of the array.

Output

Print the minimum number of moves.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
5
3 2 5 1 7

Output:
5
'''

def solution_4():
    n = int(input())
    a = list(map(int, input().split(' ')))
    c = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            c += (a[i] - a[i + 1])
            a[i+1]=a[i]
    print(c)

solution_4()

