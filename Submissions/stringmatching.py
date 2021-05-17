import sys

def longest_prefix_suffix( pattern ):
    n, k, = 0, len(pattern)
    lps = [0] * k
    idx = 1

    while idx < k:
        if pattern[idx] == pattern[n]:
            n += 1
            lps[idx] = n
            idx += 1
        else:
            if n != 0:
                n = lps[n-1]
            else:
                lps[idx] = 0
                idx += 1
    return lps

def kmp( text, pattern, lps ):
    n, k = len(text), len(pattern)
    txt_idx, pat_idx = 0, 0

    while txt_idx < n:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx += 1
            pat_idx += 1
        if pat_idx == k:
            print( txt_idx - k, end=" " )
            pat_idx = lps[pat_idx - 1]

        elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
            if pat_idx !=  0:
                pat_idx = lps[pat_idx -1]
            else:
                txt_idx += 1

while True:
    pattern = sys.stdin.readline().rstrip('\n')

    if pattern == '':
        exit(0)

    text = sys.stdin.readline().rstrip('\n')

    kmp( text, pattern, longest_prefix_suffix(pattern))
    print()

#
