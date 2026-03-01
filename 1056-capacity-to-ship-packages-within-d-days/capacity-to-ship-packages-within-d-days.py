class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = (low + high) // 2
            
            required_days = 1
            current_load = 0
            
            for weight in weights:
                if current_load + weight <= mid:
                    current_load += weight
                else:
                    required_days += 1
                    current_load = weight
            
            if required_days > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return low


        #greedy pattern
    """groups = 1
        curr_sum = 0

        for element in array:
            if curr_sum+element<=limit:
                curr_sum+=element
            else:
                groups+=1
                curr_sum = element"""