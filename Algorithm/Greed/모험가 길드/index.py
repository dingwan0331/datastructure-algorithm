def form_max_group(n:int,x:str) -> int:
    fears = sorted(list(map(int,x.split(' '))))
    group = 0
    result = 0

    for fear in fears:
        # 모험가를 그룹에 포함시키기
        group += 1
        # 모험가의 공포도보다 그룹인원이 크거나 같으면
        if group >= fear:
            # 1개 그룹을 완료
            result += 1
            # 그룹을 초기화
            group = 0
    return group