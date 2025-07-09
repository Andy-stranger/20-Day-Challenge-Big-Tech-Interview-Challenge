def minRemoveToMakeValid(self, s: str) -> str:
    st1 = []
    for i in range(len(s)):
        if s[i] == '(':
            st1.append(i)
        elif s[i] == ')':
            if not st1:
                st1.append(i)
            else:
                st1.pop()
    remove_set1 = set(st1)
    s = ''.join([c for i,c in enumerate(s) if i not in remove_set1])
    
    st2 = []
    for i in reversed(range(len(s))):
        if s[i] == ')':
            st2.append(i)
        elif s[i] == '(':
            if not st2:
                st2.append(i)
            else:
                st2.pop()
    remove_set2 = set(st2)
    return ''.join([c for i,c in enumerate(s) if i not in remove_set2])