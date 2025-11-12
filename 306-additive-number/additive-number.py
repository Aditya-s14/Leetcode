class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Try all possible splits for first and second numbers
        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                
                # Skip if number has leading zeros (except single zero)
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                
                # Start checking recursively
                if self.is_valid(num[j:], int(first), int(second)):
                    return True
        return False

    def is_valid(self, remaining, a, b):
        if not remaining:
            return True
        
        sum_str = str(a + b)
        if not remaining.startswith(sum_str):
            return False
        
        return self.is_valid(remaining[len(sum_str):], b, a + b)
