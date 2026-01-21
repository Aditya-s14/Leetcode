class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            need = target-num

            if need in hashmap:
                return [hashmap[need],i+1]
            
            hashmap[num]=i+1

              


        