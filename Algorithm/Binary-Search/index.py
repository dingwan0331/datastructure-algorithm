# 반복문을 통한 이진탐색 구현
def binary_search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    # start가 end보다 높거나 같은경우 탐색 종료
    while start <= end:
        # mid는 start 와 end의 중간값 정수로 구하기 위해 내림 나눗셈을 한다.
        mid = (start + end ) // 2
        # 탐색범위의 중간값이 target과 일치하면 현재 중간 인덱스 반환
        if nums[mid] == target:
            return mid
        
        # 탐색범위의 중간값이 target보다 작으면 탐색범위를 절반보다 앞쪽으로 좁힌다.
        if nums[mid] < target:
            end = mid - 1
        # 탐색범위의 중간값이 target보다 크면 탐색범위를 절반보다 뒷쪽으로 좁힌다.   
        elif nums[mid] > target:
            start = mid + 1
    # 찾는 값이 없을경우 None 반환
    return None

def recursion_binary_search(nums: list[int], start: int, end: int, target: int) -> int:
    # start 가 end가 높은경우 == 탐색완료하였지만 값을 찾지 못함
    if start > end:
        return None
    mid = (start + end) //2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        end = mid - 1
        return recursion_binary_search(nums, start, end, target)
    if nums[mid] > target:
        start = mid + 1
        return recursion_binary_search(nums, start, end, target)