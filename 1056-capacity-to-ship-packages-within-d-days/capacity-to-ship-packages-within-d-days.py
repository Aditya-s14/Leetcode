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