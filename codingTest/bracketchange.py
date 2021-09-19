def pair(p):#균형잡힌 괄호 문자열
    cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            cnt-=1
    return True
def balance(p):#u,v 나누어야 할 구간 리턴
    cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return i

def solution(p):
    ans=''
    if p=='':
        return ans
    idx=balance(p)
    u=p[:idx+1]
    v=p[idx+1:]
    if pair(u):
        ans=u+solution(v)
    else:
        ans+='('
        ans+=solution(v)
        ans+=')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        ans+="".join(u)
    return ans
