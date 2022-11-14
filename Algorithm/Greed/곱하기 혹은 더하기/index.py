def choose_plus_or_multiply(str):
    # 초기 수 세팅
    answer = int(str[0])
    for i in str:
        # 현재 계산된 값혹인 이제 계산할값이 1보다 작거나 같으면 + 연산
        if answer <= 1 or int(i) <= 1:
            answer += int(i)
        else:
            answer *= int(i)  
    return answer      


# def choose_plus_or_multiply(str):
    # answer = int(str[0]) + int(str[1])if int(str[0]) >= 1 or int(str[1]) >= 1 else int(str[0]) * int(str[1])
    # for i in str[2:]:
    #     if int(i) <= 1:
    #         answer += int(i)
    #     else:
    #         answer *= int(i)
    # return answer