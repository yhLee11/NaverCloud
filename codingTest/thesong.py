def shap_to_lower(s):
    s=s.replace('A#','a').replace('F#','f').replace('C#','c').replace('D#','d').replace('G#','g')
    return s
def solution(m, musicinfos):
    #재생 시간과 제공된 악보
    #음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
    info={}
    total=0
    m=shap_to_lower(m)

    for i in musicinfos:
        lst=i.split(',')
        start,end=list(map(int,lst[0].split(':'))),list(map(int,lst[1].split(':')))
        lst[3]=shap_to_lower(lst[3])
        total=(end[0]-start[0])*60+(end[1]-start[1])
        music=''
        if total>len(lst[3]):
            div=divmod(total,len(lst[3]))
            music=lst[3]*div[0]+lst[3][:div[1]]
            print(div,music,len(music))
        else:#길이가 같거나 작을때
            music=lst[3][:total]
            print(music,len(music))
        info[lst[2]]=music
    print(info)
    res=""
    ans=""
    for k,v in info.items():
        if m in v:
            if ans=="":
                ans = k
                res = v
            else:
                if len(res) < len(v):
                    ans = k
                    res = v

    print(res)
    if res:
        return ans
    else:
        return "(None)"
