def solution(N, stages):

    res=[]
    for i in range(N):
        notComp=0
        passing=0
        for v in stages:
            # print(v,i+1)
            if v==i+1:
                notComp+=1
                passing+=1
            elif v>i+1:
                passing+=1

        if notComp==0:
            res.append((i+1,0))
        else:
            res.append((i+1,notComp/passing))


    res.sort(key=lambda x:(-x[1]))
    print(res)
    temp=[]
    for i in res:
        temp.append(i[0])
    return temp
