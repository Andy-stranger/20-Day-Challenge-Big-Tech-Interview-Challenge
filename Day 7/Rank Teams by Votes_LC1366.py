from collections import defaultdict

def rankTeams(self, votes) -> str:
    tot = len(votes[0])
    mapp = defaultdict(lambda : [0]*tot)
    for vote in votes:
        for pos,val in enumerate(vote):
            mapp[val][pos] -= 1
    mapp = sorted(mapp.items(), key = lambda item: (item[1],item[0]))
    return ''.join(item[0] for item in mapp)