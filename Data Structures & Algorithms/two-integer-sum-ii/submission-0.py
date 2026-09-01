class Solution:
    def twoSum(self, numbers: List[int], target: int):
        theDict={}
        for i in range(len(numbers)):
            val=target-numbers[i]
             
            if val in theDict:
                if theDict[val]!=i+1:
                    return [theDict[val],i+1]

            theDict[numbers[i]]=i+1
        
        return []
        