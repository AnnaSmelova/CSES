'''
6. Number Spiral
Time limit: 1.00 s Memory limit: 512 MB
A number spiral is an infinite grid whose upper-left square has number 1.
Here are the first five layers of the spiral: :(

Your task is to find out the number in row y and column x.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, each containing integers y and x.

Output

For each test, print the number in row y and column x.

Constraints
1≤t≤105
1≤y,x≤109
Example

Input:
3
2 3
1 1
4 2

Output:
8
1
15
'''


def get_num(i, j):
    if i == j:
        return 1 + i * (i - 1)
    if j > i:
        if j % 2 == 0:
            return get_num(j, j) - (j - i)
        else:
            return get_num(j, j) + (j - i)
    else:
        if i % 2 == 0:
            return get_num(i, i) + (i - j)
        else:
            return get_num(i, i) - (i - j)



def main():
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        print(get_num(y, x))


main()