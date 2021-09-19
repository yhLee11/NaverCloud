def solution(lines):
    #끝시간2000초-1000 =1000밀리초
    #term=999밀리초면 1초안에 겹치는거임
    ans=0
    start_time=[]
    end_time=[]
    for t in lines:
        time=t.split(" ")
        start_time.append(get_start_time(time[1],time[2]))
        end_time.append(get_time(time[1]))

    for i in range(len(lines)):
        cnt=0
        cur_end_time=end_time[i]
        for j in range(i,len(lines)):
            if cur_end_time>=start_time[j]-999:
                cnt+=1
        ans=max(ans,cnt)
    return ans

    print(int(.008))
def get_time(time):#대소비교를 하기 위해서 정수형 변환
    hour=int(time[:2])*3600#01*3600=3600
    minute=int(time[3:5])*60#00*60=0
    second=int(time[6:8])#04
    millisecond=int(time[9:])
    return (hour+minute+second)*1000+millisecond
def get_start_time(time,duration_time):
    n_time=duration_time[:-1]
    int_duration_time=int(float(n_time)*1000)
    return get_time(time)-int_duration_time+1
