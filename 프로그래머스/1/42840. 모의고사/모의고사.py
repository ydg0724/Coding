def solution(answers):

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    result = []
    for i,answer in enumerate(answers):
        if one[i%len(one)] == answer:
            correct[0] +=1

        if two[i % len(two)] ==answer:
            correct[1] +=1

        if three[i % len(three)] == answer:
            correct[2] += 1

    for i,corrects in enumerate(correct):
        if max(correct)==corrects:
            result.append(i+1)
            
    return result
