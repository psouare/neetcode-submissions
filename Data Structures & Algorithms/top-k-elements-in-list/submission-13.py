class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        bucket = [[] for _ in range(len(nums) + 1)]
        for f,i in freq.items():
            bucket[i].append(f)
        
        res=[]
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res

