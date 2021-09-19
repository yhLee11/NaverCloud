"""
2,5,8,0에서 현재 위치 절댓값 구하고
3으로 나눈 뒤 몫과 나머지 더하면 거리 구할 수 있음
*:10 0:11 #:12로 설정
"""
def solution(numbers, hand):
    #'*'10 '0':11 '#'12
    lthumb=10
    rthumb=12
    ldist,rdist=-1,-1
    res=''

    for n in numbers:
        if n in [1,4,7]:
            # print('lth',n)
            lthumb=n
            res+='L'
        elif n in [3,6,9]:
            # print('rth',n)
            rthumb=n
            res+='R'
        else:#거리 측정
            n=11 if n==0 else n
            rdist=abs(n-rthumb)
            ldist=abs(n-lthumb)
            if sum(divmod(rdist,3))<sum(divmod(ldist,3)):
                rthumb=n
                res+='R'
            elif sum(divmod(rdist,3))>sum(divmod(ldist,3)):
                lthumb=n
                res+='L'
            else:
                if hand=='right':
                    rthumb=n
                    res+='R'
                else:
                    lthumb=n
                    res+='L'

    return res
