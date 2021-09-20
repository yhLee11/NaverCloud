dx=[1,2,1,0,0,-1]
dy=[0,0,1,1,2,1]
def search(x,y,room):
    for z in range(6):
        nx=dx[z]+x
        ny=dy[z]+y
        if 0<=nx<5 and 0<=ny<5:
            if z==0 or z==3:
                if room[ny][nx]=='P':
                    return False
            elif z==1:
                if room[ny][nx]=='P' and room[ny][nx-1]=='O':
                    return False
            elif z==2:
                if room[ny][nx]=='P':
                    if room[ny][nx-1]=='O' or room[ny-1][nx]=='O':
                        return False
            elif z==4:
                if room[ny][nx]=='P' and room[ny-1][nx]=='O':
                    return False
            elif z==5:
                if room[ny][nx]=='P':
                    if room[ny][nx+1]=='O' or room[ny-1][nx]=='O':
                        return False
    return True

def solution(places):
    #맨해튼거리(r1,c1)(r2,c2) |r1-r2|+|c1-c2|<=2이면 불가능
    #파티션 있으면 맨해튼 무시 가능
    #p:앉은자리, 0:빈테이블, X:파티션
    #places 한개 리스트가 방 하나
    ans=[]
    for room in places:
        #room:방하나
        itsOk=True
        for i in range(5):
            for j in range(5):
                if room[i][j]=='P':#주변 검사 실행
                    itsOk=search(j,i,room)
                if not itsOk:
                    break
            if not itsOk:
                break
        if itsOk:
            ans.append(1)
        else:
            ans.append(0)

    return ans
