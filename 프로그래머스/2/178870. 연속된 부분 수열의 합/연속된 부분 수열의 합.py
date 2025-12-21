def solution(sequence, k):
    left = 0
    current_sum = 0
    answer = [0, len(sequence) - 1] 

    for right in range(len(sequence)):
        current_sum += sequence[right]

        while current_sum > k:
            current_sum -= sequence[left]
            left += 1

        if current_sum == k:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]

    return answer