def solution(s):
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    st=''
    num=''
    isalpha=False
    isnum=False
    res=''
    for i in s:
        if i.isalpha():
            if isnum:#숫자에서 알파벳으로 변경될 때
                print('3',num)
                res+=num
                num=''
                st+=i
                isnum=False
            else:#계속 알파벳일때
                st+=i
                if st in dic:
                    print('2',st)
                    res+=dic[st]
                    st=''
                isalpha=False
        elif i.isdigit():
            if isalpha:#직전까지 알파벳이었을때
                st=''
                isalpha=False
                num+=i
            else:#
                isnum=True
                num+=i


    if s[-1].isdigit():
        res+=num
    print(res)
    return int(res)
