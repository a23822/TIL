def solution(genres, plays):
    
    answer = []
    
    # 장르마다 플레이 횟수를 정한다.
    genreDic = {}
    playDic = {}
    # {'장르' : [total, (고유번호, 재생 수) , ...]}
    dic = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if not g in dic.keys():
            dic[g] = []
            dic[g].append(p)
            dic[g].append((i,p))
        else:
            dic[g].append((i,p))
            dic[g][0] += p
    
    # 장르별로 구분하고 두 개씩 모은다.
    sortArr = sorted(dic, key = lambda k : dic[k][0], reverse=True)
    for item in sortArr:
        #장르 내에서 재생 수에 따라 구분
        temp = dic[item][1:]
        temp.sort(key = lambda temp : temp[1], reverse=True)
        #rint(temp)
        for n in range(len(temp)):
            if n < 2:
                answer.append(temp[n][0])
            else:
                break
    # print("총")
    # print(dic)
    
    return answer

"""
다른사람 풀이
ZIP사용
"""

from collections import defaultdict as dd

def solution2(genres, plays):
    playOfGenre = dd(int)
    songIdAndPlay = dd(list)
    for songId, (genre,play) in enumerate(zip(genres, plays)):
        playOfGenre[genre] += play
        songIdAndPlay[genre].append((songId,play))

    playOfGenre = sorted(playOfGenre.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for genre,play in playOfGenre:
        songIdAndPlay[genre].sort(key=lambda x: x[1], reverse=True)
        answer += songIdAndPlay[genre][:2]

    answer = [a[0] for a in answer]
    return answer

