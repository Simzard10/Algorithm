def solution(triangle):
    height = len(triangle)-1
    for i in range(height-1, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    return triangle[0][0]