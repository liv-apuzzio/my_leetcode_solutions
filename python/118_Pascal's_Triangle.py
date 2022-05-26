class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1 = [1]
        pascals = [[1], [1,1]]
        if numRows == 0:
            return [[]]
        elif numRows == 1:
            return [pascals[0]]
        elif numRows == 2:
            return pascals
        else:
            for i in range(1, numRows - 1):
                for j in range(len(pascals[i])-(len(pascals[i])-1)):
                    for k in range(j+1, len(pascals[i])):
                        list1.append(pascals[i][j] + pascals[i][k])
                        j += 1
                        k +=1
                list1.append(1)
                pascals.append(list1)
                list1 = [1]
                i += 1
            return pascals