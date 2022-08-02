def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = []
    # -1000 means haven't been visited 1 means visited
    visit = [[-1000 for i in range(0,len(matrix[0])+2)] for j in range(0,len(matrix)+2)]
    for i in range(0,len(visit)):
        visit[i][0] = 1
        visit[i][len(visit[i])-1] = 1
    visit[0] = [1 for i in range(0,len(visit[0]))]
    visit[len(visit)-1] = [1 for i in range(0,len(visit[0]))]
    directions = [  [0,1],  #right
                    [1,0],  #down
                    [0,-1], #left
                    [-1,0]]  #up 
    startPoint = [1,1]
    currPoint = startPoint
    while(visit[currPoint[0]-1][currPoint[1]] == -1000 or visit[currPoint[0]+1][currPoint[1]] == -1000 or visit[currPoint[0]][currPoint[1]-1] == -1000 or visit[currPoint[0]][currPoint[1]+1] == -1000):
        for direction in directions:
            currPoint = startPoint
            visit[currPoint[0]][currPoint[1]] = -1000
            while visit[currPoint[0]+direction[0]][currPoint[1]+direction[1]] == -1000:
                ans.append(matrix[currPoint[0]-1][currPoint[1]-1])
                visit[currPoint[0]][currPoint[1]] = 1
                currPoint[0] += direction[0]
                currPoint[1] += direction[1]
            startPoint = [currPoint[0],currPoint[1]]
    ans.append(matrix[currPoint[0]-1][currPoint[1]-1])
    return ans

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))