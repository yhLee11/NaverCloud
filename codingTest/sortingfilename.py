def solution(files):
    #이름순정렬1>9,숫자가 포함된 파일 목록
    #파일명에 포함된 숫자를 반영한 정렬 기능
    #숫자가 나오면 자름
    #앞에 0 무시
    lst=[]
    for f in files:
        num=''
        isNum=False
        head=''
        tail=''
        one=[]
        for i in f: #onefile=>muzi1.txt
            if not isNum and not i.isdigit():
                head+=i
            elif i.isdigit() and not isNum:
                isNum=True
                num+=i
            elif i.isdigit() and isNum:
                num+=i
            else:
                break

        # print(head,num,tail)
        lst.append([head,num,f])
    print(lst)
    lst.sort(key=lambda x: [x[0].upper(),int(x[1])])
    res=[]
    print(lst)
    for i in lst:
        res.append(i[2])
    print(res)
    return res
