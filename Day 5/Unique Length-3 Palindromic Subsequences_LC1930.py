from collections import defaultdict

def countPalindromicSubsequence(s: str) -> int:
    right = defaultdict(int)
    res = set()
    left = set()
    for a in s:
        right[a] += 1
    for a in s:
        if right[a]:
            right[a] -= 1
        for i in range(26):
            cur = chr(ord('a')+i)
            if cur in left and right[cur]:
                res.add(a+""+cur)
        left.add(a)
    return len(res)