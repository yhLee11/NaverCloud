from itertools import combinations as combi
def solution(relation):
    #최소성 각자 꼭 유일해야함 꼭 필요한 속성들로만 구성?
    #이름전공학년에서 이름 빼면 유일성 충족 불가
    row=len(relation)
    col=len(relation[0])
    candi=[]
    for i in range(1,col+1):
        candi.extend(combi(range(col),i))
        # print(candi)

    unique=[]
    for c in candi:
        tmp=[tuple([item[i] for i in c]) for item in relation]
        if len(set(tmp))==row:
            unique.append(c)
#         print(tmp)
    # print(unique)

    ans=set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i])==len(set(unique[i])&set(unique[j])):
                print(set(unique[i])&set(unique[j]))
                ans.discard(unique[j])
    return len(ans)
