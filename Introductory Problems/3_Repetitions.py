'''
3. Repetitions
You are given a DNA sequence: a string consisting of characters A, C, G, and T.
Your task is to find the longest repetition in the sequence.
This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
'''

def solution_3():
    s = input()
    count = 1
    max_count = 0
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
            prev = s[i]
    max_count = max(count, max_count)
    print(max_count)

solution_3()