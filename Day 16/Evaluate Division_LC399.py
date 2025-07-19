from collections import defaultdict, deque, List

def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj = defaultdict(list)
    for e,v in zip(equations,values):
        a,b = e
        adj[a].append([b,v])
        adj[b].append([a,1/v])
    
    def bfs(src,tar):
        if src not in adj or tar not in adj:
            return -1
        q , vis = deque() , set()
        q.append([src,1])
        vis.add(src)
        while q:
            cn , cw = q.popleft()
            if cn == tar:
                return cw
            for nn , nw in adj[cn]:
                if nn not in vis:
                    q.append([nn,nw*cw])
                    vis.add(nn)
        return -1
    
    return [bfs(a,b) for a,b in queries]