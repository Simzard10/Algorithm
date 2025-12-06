from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current, depth = queue.popleft()

        for word in words:
            if word in visited:
                continue

            diff = 0
            for i in range(len(current)):
                if current[i] != word[i]:
                    diff += 1

            if diff == 1:
                if word == target:
                    return depth + 1
                visited.add(word)
                queue.append((word, depth + 1))

    return 0