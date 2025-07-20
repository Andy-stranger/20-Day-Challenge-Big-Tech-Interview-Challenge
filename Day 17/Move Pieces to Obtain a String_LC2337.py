def canChange(self, start: str, target: str) -> bool:
    if len(start) != len(target):
        return False
    src_ind = 0
    tar_ind = 0
    left_limit = -1
    while src_ind < len(start):
        while src_ind < len(start) and start[src_ind] == '_':
            src_ind += 1
        while tar_ind < len(target) and target[tar_ind] == '_':
            tar_ind += 1
        if src_ind == len(start) and tar_ind == len(target):
            return True
        if src_ind < len(start) and tar_ind < len(target):
            if start[src_ind] != target[tar_ind] or (start[src_ind] == 'L' and (tar_ind <= left_limit or src_ind < tar_ind)) or (start[src_ind] == 'R' and src_ind > tar_ind):
                return False
        left_limit = tar_ind
        src_ind += 1
        tar_ind += 1
    while src_ind < len(start) and start[src_ind] == '_':
        src_ind += 1
    while tar_ind < len(target) and target[tar_ind] == '_':
        tar_ind += 1
    return src_ind == len(start) and tar_ind == len(target)