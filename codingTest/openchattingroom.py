def solution(record):
    res=[]
    info={}
    for i in record:
        lst=i.split(' ')
        if lst[0]=='Leave':
            res.append([lst[1],'님이 나갔습니다.'])
        else:
            info[lst[1]]=lst[2]
            if lst[0]=='Enter':
                res.append([lst[1],'님이 들어왔습니다.'])

    for i,v in enumerate(res):
        res[i]=info[v[0]]+v[1]
    return res
