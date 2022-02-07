def solution(number):
    # create a list to populate
    answers = []
    
    # loop through all numbers in the range
    for i in range(number):
        # if divisible by 3 or 5 and within range
        if (i%3==0 or i%5==0) and i<number and i>0:
            # add to the answers list
            answers.append(i)
        
    # return the sum of the answers
    return sum(answers)
print(solution(45))