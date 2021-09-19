from itertools import combinations as combi
def solution(relation):

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
