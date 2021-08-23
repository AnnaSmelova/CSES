'''
11. Coin Piles
Time limit: 1.00 s Memory limit: 512 MB
You have two coin piles containing a and b coins.
On each move, you can either remove one coin from the left pile and two coins from the right pile,
or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

Input

The first input line has an integer t: the number of tests.

After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output

For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints
1≤t≤105
0≤a,b≤109
Example

Input:
3
2 1
2 2
3 3

Output:
YES
NO
YES
'''

def get_result(a, b):
    if a == 0:
        if a != b:
            return 'NO'
        else:
            return 'YES'
    elif b == 0:
        return 'NO'
    else: # a!=0 and b!=0
        if (a + b) % 3 != 0:
            return 'NO'
        else:
            if ((a / b) > 2) or ((b / a) > 2):
                return 'NO'
            else:
                return 'YES'


def solution_11():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(get_result(a, b))


solution_11()

