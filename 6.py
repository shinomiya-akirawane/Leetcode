class Solution:
    def str2list(self,s):
        res = []
        for letter in s:
            res.append(letter)
        return res

    def buildModel(self,s,numRows):
        model = []
        s:list = self.str2list(s)
        full_col_num = numRows
        col_num = (((len(s)//(numRows+numRows-2))+1)*(numRows-1))+1
        for i in range(0,col_num+1):
            model.append([0 for x in range(0,full_col_num)])
        for i in range(0,col_num+1):
            if i % (numRows-1) == 0:
                for k in range(0,full_col_num):
                    try:
                        model[i][k] = s.pop(0)
                    except:
                        return model
            else:
                group_num = i % (numRows-1)
                try:
                    model[i][full_col_num-1-group_num] = s.pop(0)
                except:
                    return model
        return model

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        model = self.buildModel(s,numRows)
        row_length = len(model)
        col_length = len(model[0])
        ans = ''
        for row in range(0,col_length):
            for col in range(0,row_length):
                if model[col][row] != 0:
                    ans += model[col][row]
        return ans
s = Solution()
s.convert("PAYPALISHIRING",9)