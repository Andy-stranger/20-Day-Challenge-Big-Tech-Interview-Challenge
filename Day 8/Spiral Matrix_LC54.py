def spiralOrder(matrix):
    rs , re = 0 , len(matrix)-1
    cs , ce = 0 , len(matrix[0])-1
    res = []
    while rs <= re and cs <= ce:
        
        for i in range(cs,ce+1):
            res.append(matrix[rs][i])
        rs += 1

        for i in range(rs,re+1):
            res.append(matrix[i][ce])
        ce -= 1

        if rs <= re:
            for i in range(ce,cs-1,-1):
                res.append(matrix[re][i])
            re -= 1
        
        if cs <= ce:
            for i in range(re,rs-1,-1):
                res.append(matrix[i][cs])
            cs += 1
    
    return res