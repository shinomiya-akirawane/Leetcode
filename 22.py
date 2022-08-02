def generateParenthesis(n: int) -> list[str]:
        ans = []
        def dfs(n,lNum,rNum,str):
            if lNum == n and rNum == n:
                ans.append(str)
            else:
                if lNum < n:
                    dfs(n,lNum+1,rNum,str+'(')
                if rNum < n and lNum > rNum:
                    dfs(n,lNum,rNum+1,str+')')
        dfs(n,0,0,'')
        return ans

generateParenthesis(3)