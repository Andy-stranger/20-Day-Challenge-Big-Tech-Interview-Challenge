from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for st in strs:
        key = ''.join(sorted(st))
        if key in res:
            res[key].append(st)
        else:
            res[key] = [st]
    return [a for a in res.values()]