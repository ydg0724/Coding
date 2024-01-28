def solution(nums):
    tmp = []
    for i in range(len(nums)):
        if len(tmp) >= len(nums)/2:
            break
        if nums[i] not in tmp:
            tmp.append(nums[i])

    answer = len(tmp)

    return answer